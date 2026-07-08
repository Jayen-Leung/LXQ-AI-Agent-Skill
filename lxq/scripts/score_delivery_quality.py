#!/usr/bin/env python3
"""Score a Chinese LXQ customer-delivery scheme with transparent heuristics."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_SECTIONS = [
    "拟定题目", "研究背景与临床问题", "研究假说", "研究目标",
    "主要研究内容", "拟解决的关键问题", "研究对象与样本量",
    "分组、检测指标与随访节点", "统计学与模型构建", "技术路线",
    "创新点", "可行性分析", "风险与替代方案", "预期成果",
]
AI_PHRASES = [
    "多维度", "多层次", "系统阐明", "具有重要理论意义和实践价值",
    "为临床诊疗提供新思路", "为后续研究奠定基础", "有望推动",
    "进一步丰富", "提供理论依据",
]
HIGH_COST_METHODS = [
    "单细胞测序", "单细胞组学", "空间转录组", "空间组学",
    "大规模代谢组", "大规模蛋白组", "多中心前瞻性大队列",
    "完整动物机制验证", "类器官大规模筛选", "多组学整合",
]
UNCERTAIN_AS_FACT = [
    r"前期(?:研究)?已证实", r"已建立(?:稳定的)?\d+例", r"伦理(?:批准|批件|编号)(?:为|是|：)",
    r"已经明确(?:证实|证明)", r"必然(?:改善|提高|降低)",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Chinese customer-delivery Markdown or text")
    parser.add_argument("--budget", type=float, default=None, help="Budget in CNY")
    parser.add_argument(
        "--fail-below", type=int, default=None,
        help="Return exit code 3 when the score is below this threshold",
    )
    return parser.parse_args()


def infer_budget(text: str) -> float | None:
    patterns = [
        r"(?:经费|预算)(?:上限|总额|规模)?[^\d]{0,10}(\d+(?:\.\d+)?)\s*万元",
        r"(?:经费|预算)(?:上限|总额|规模)?[^\d]{0,10}(\d+(?:\.\d+)?)\s*万",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1)) * 10000
    return None


def find_budget_warnings(text: str, budget: float | None) -> list[str]:
    if budget is None or budget > 30000:
        return []
    return [f"经费≤3万元但方案包含高成本技术：{method}" for method in HIGH_COST_METHODS if method in text]


def has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def main() -> int:
    args = parse_args()
    if not args.document.is_file():
        print(json.dumps({"error": f"document not found: {args.document}"}, ensure_ascii=False))
        return 2
    text = args.document.read_text(encoding="utf-8-sig")
    budget = args.budget if args.budget is not None else infer_budget(text)

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    field_checks = {
        "sample_size": has_any(text, ["样本量", "例患者", "例受试者", "n="]),
        "inclusion_criteria": has_any(text, ["纳入标准", "入组标准", "入选标准"]),
        "exclusion_criteria": has_any(text, ["排除标准", "排除条件"]),
        "grouping": has_any(text, ["分组", "对照组", "观察组", "训练集"]),
        "primary_endpoint": has_any(text, ["主要终点", "主要结局"]),
        "secondary_endpoint": has_any(text, ["次要终点", "次要结局"]),
        "measurements": has_any(text, ["检测指标", "测量指标", "主要指标", "评价指标"]),
        "statistics": has_any(text, ["统计方法", "统计学", "回归模型", "生存分析", "置信区间"]),
        "risk": "风险" in text,
        "alternative": has_any(text, ["替代方案", "替代路线", "备选方案"]),
    }
    missing_fields = [name for name, passed in field_checks.items() if not passed]
    ai_style_flags = [phrase for phrase in AI_PHRASES if phrase in text]
    uncertainty_flags = [pattern for pattern in UNCERTAIN_AS_FACT if re.search(pattern, text)]
    budget_method_warnings = find_budget_warnings(text, budget)

    score = 100
    score -= min(42, 3 * len(missing_sections))
    score -= min(40, 5 * len(missing_fields))
    score -= min(12, 2 * len(ai_style_flags))
    score -= min(20, 10 * len(uncertainty_flags))
    score -= min(24, 12 * len(budget_method_warnings))
    score = max(0, score)

    major_issues: list[str] = []
    if missing_sections:
        major_issues.append("客户交付默认章节不完整")
    if any(not field_checks[name] for name in ("sample_size", "inclusion_criteria", "exclusion_criteria")):
        major_issues.append("研究对象或样本设计字段不完整")
    if any(not field_checks[name] for name in ("primary_endpoint", "secondary_endpoint", "statistics")):
        major_issues.append("终点或统计字段不完整")
    if uncertainty_flags:
        major_issues.append("存在需要证据核验的既定事实表述")
    if budget_method_warnings:
        major_issues.append("经费与技术复杂度可能不匹配")

    minor_issues: list[str] = []
    if ai_style_flags:
        minor_issues.append("存在高频AI模板表达")
    if budget is None:
        minor_issues.append("未识别到经费，无法执行预算匹配检查")

    if score >= 85 and not major_issues:
        decision = "pass"
    elif score >= 65:
        decision = "conditional_pass"
    else:
        decision = "fail"

    recommendations = [f"补充章节：{name}" for name in missing_sections]
    recommendations += [f"补充字段：{name}" for name in missing_fields]
    if ai_style_flags:
        recommendations.append("应用中文去AI味过滤器，用具体对象、指标、方法和结局替换空话")
    if uncertainty_flags:
        recommendations.append("核验前期、伦理和既定结果；无法核验时改为拟采用或需确认")
    if budget_method_warnings:
        recommendations.append("按预算缩减高成本技术，或提供真实报价、平台和追加经费依据")

    payload = {
        "score": score,
        "decision": decision,
        "budget_cny": budget,
        "major_issues": major_issues,
        "minor_issues": minor_issues,
        "missing_sections": missing_sections,
        "missing_fields": missing_fields,
        "ai_style_flags": ai_style_flags,
        "uncertainty_as_fact_flags": uncertainty_flags,
        "budget_method_warnings": budget_method_warnings,
        "recommendations": recommendations,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.fail_below is not None and score < args.fail_below:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
