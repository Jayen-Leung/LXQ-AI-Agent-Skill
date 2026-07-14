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
    "进一步丰富", "提供理论依据", "填补国内外空白", "具有广阔应用前景",
]
HIGH_COST_METHODS = [
    "单细胞测序", "单细胞组学", "空间转录组", "空间组学",
    "大规模代谢组", "大规模蛋白组", "多中心前瞻性大队列",
    "完整动物机制验证", "类器官大规模筛选", "多组学整合",
    "scRNA-seq", "single-cell", "Visium", "WES", "WGS", "全外显子",
    "全基因组", "空间蛋白组", "大规模质谱",
]
UNCERTAIN_AS_FACT = [
    r"前期(?:研究)?已证实", r"已(?:收集|纳入|建立)(?:稳定的)?\d+例", r"伦理(?:已)?(?:批准|批件|编号)(?:为|是|：)?",
    r"已经明确(?:证实|证明)", r"已证实(?:机制|通路|作用)", r"必然(?:改善|提高|降低)",
    r"保证(?:中标|发表|接收|有效)", r"确保(?:中标|发表|接收|有效)",
]
UNCERTAINTY_MARKERS = ["拟", "建议", "需进一步确认", "待确认", "AUTHOR_INPUT_NEEDED", "EVIDENCE_NEEDED"]


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


def has_numbered_sample_size(text: str) -> bool:
    if re.search(r"(?:样本量|病例数|受试者|患者)[^\n。；;]{0,30}(?:\d+\s*(?:例|名|人)|n\s*[=＝]\s*\d+)", text, re.I):
        return True
    if re.search(r"(?:\d+\s*(?:例|名|人)|n\s*[=＝]\s*\d+)[^\n。；;]{0,30}(?:患者|受试者|样本|病例)", text, re.I):
        return True
    return has_any(text, ["样本量估算", "样本量计算", "样本量需进一步确认", "AUTHOR_INPUT_NEEDED: 样本量"])


def find_unverified_fact_flags(text: str) -> list[str]:
    flags: list[str] = []
    for pattern in UNCERTAIN_AS_FACT:
        for match in re.finditer(pattern, text):
            window = text[max(0, match.start() - 30): match.end() + 30]
            if not has_any(window, UNCERTAINTY_MARKERS):
                flags.append(pattern)
                break
    return flags


def main() -> int:
    args = parse_args()
    if not args.document.is_file():
        print(json.dumps({"error": f"document not found: {args.document}"}, ensure_ascii=False))
        return 2
    text = args.document.read_text(encoding="utf-8-sig")
    budget = args.budget if args.budget is not None else infer_budget(text)

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    field_checks = {
        "sample_size": has_numbered_sample_size(text),
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
    uncertainty_flags = find_unverified_fact_flags(text)
    budget_method_warnings = find_budget_warnings(text, budget)
    hard_flags = []
    if uncertainty_flags:
        hard_flags.append("unverified_fact_as_established")
    if budget_method_warnings:
        hard_flags.append("low_budget_high_cost_methods")
    if not field_checks["sample_size"]:
        hard_flags.append("sample_size_missing_or_unbounded")

    score = 100
    score -= min(42, 3 * len(missing_sections))
    score -= min(40, 5 * len(missing_fields))
    score -= min(12, 2 * len(ai_style_flags))
    score -= min(20, 10 * len(uncertainty_flags))
    score -= min(24, 12 * len(budget_method_warnings))
    score -= min(18, 6 * len(hard_flags))
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
    readiness = "ready_to_use" if decision == "pass" else "conditional"
    if hard_flags:
        readiness = "blocked" if decision == "fail" else "needs_author_input"

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
        "hard_flags": hard_flags,
        "readiness": readiness,
        "recommendations": recommendations,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.fail_below is not None and score < args.fail_below:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
