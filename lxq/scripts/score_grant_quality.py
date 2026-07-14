#!/usr/bin/env python3
"""Score an LXQ Chinese grant proposal with transparent content heuristics."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from score_delivery_quality import (
    AI_PHRASES,
    find_budget_warnings,
    find_unverified_fact_flags,
    has_numbered_sample_size,
    infer_budget,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="Chinese grant proposal Markdown or text")
    parser.add_argument("--budget", type=float, default=None, help="Budget in CNY")
    parser.add_argument(
        "--fail-below", type=int, default=None,
        help="Return exit code 3 when the score is below this threshold",
    )
    return parser.parse_args()


def has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def section_body(text: str, terms: list[str]) -> str:
    lines = text.splitlines()
    start: int | None = None
    body: list[str] = []
    for index, line in enumerate(lines):
        if line.lstrip().startswith("#") and has_any(line, terms):
            start = index + 1
            break
    if start is None:
        return ""
    for line in lines[start:]:
        if line.lstrip().startswith("#"):
            break
        if line.strip():
            body.append(line.strip())
    return "\n".join(body)


def main() -> int:
    args = parse_args()
    if not args.document.is_file():
        print(json.dumps({"error": f"document not found: {args.document}"}, ensure_ascii=False))
        return 2
    text = args.document.read_text(encoding="utf-8-sig")
    budget = args.budget if args.budget is not None else infer_budget(text)
    background = section_body(text, ["研究背景", "立项依据", "临床问题"])
    objectives = section_body(text, ["研究目标"])
    contents = section_body(text, ["研究内容"])
    innovation = section_body(text, ["创新点"])
    risk = section_body(text, ["风险与替代", "风险"])

    checks = {
        "specific_significance": bool(background) and has_any(background, ["临床", "患者", "人群", "结局", "诊疗", "管理"]),
        "clear_gap": has_any(text, ["缺口", "不足", "尚不清楚", "尚未明确", "未解决", "困难在于", "缺乏"]),
        "measurable_objectives": bool(objectives) and has_any(objectives, ["评估", "比较", "估计", "验证", "构建", "量化"]),
        "content_objective_alignment": bool(objectives) and bool(contents),
        "specific_innovation": len(innovation) >= 30 and has_any(innovation, ["人群", "指标", "方法", "验证", "时间点", "数据"]),
        "sample_size_basis": has_numbered_sample_size(text) and has_any(text, ["依据", "计算", "效应量", "事件率", "把握度", "精度", "失访", "需进一步确认"]),
        "statistics_match": has_any(text, ["统计方法", "回归模型", "生存分析", "混合效应", "置信区间", "多重比较"]),
        "risk_and_alternative": bool(risk) and has_any(risk, ["替代", "备选", "缓解", "预案"]),
    }
    missing_fields = [name for name, passed in checks.items() if not passed]
    ai_style_flags = [phrase for phrase in AI_PHRASES if phrase in text]
    budget_method_warnings = find_budget_warnings(text, budget)
    uncertainty_flags = find_unverified_fact_flags(text)
    hard_flags = []
    if uncertainty_flags:
        hard_flags.append("unverified_fact_as_established")
    if budget_method_warnings:
        hard_flags.append("low_budget_high_cost_methods")
    if not checks["sample_size_basis"]:
        hard_flags.append("sample_size_basis_missing_or_unbounded")

    score = 100 - 9 * len(missing_fields)
    score -= min(12, 2 * len(ai_style_flags))
    score -= min(24, 12 * len(budget_method_warnings))
    score -= min(20, 10 * len(uncertainty_flags))
    score -= min(18, 6 * len(hard_flags))
    score = max(0, score)

    major_issues: list[str] = []
    for key in ("measurable_objectives", "content_objective_alignment", "sample_size_basis", "statistics_match"):
        if not checks[key]:
            major_issues.append(f"关键基金质量项未通过：{key}")
    if budget_method_warnings:
        major_issues.append("经费与技术路线可能不匹配")
    if uncertainty_flags:
        major_issues.append("存在需要证据核验的既定事实表述")

    minor_issues: list[str] = []
    for key in ("specific_significance", "clear_gap", "specific_innovation", "risk_and_alternative"):
        if not checks[key]:
            minor_issues.append(f"需要加强：{key}")
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

    recommendations = [f"补强基金质量项：{name}" for name in missing_fields]
    if ai_style_flags:
        recommendations.append("删除空泛意义表述，改写为具体问题、对象、指标、方法和结局")
    if budget_method_warnings:
        recommendations.append("缩减高成本技术或补充报价、平台、样本和经费依据")
    if uncertainty_flags:
        recommendations.append("核验前期、伦理、样本和既定机制事实；无法核验时改为拟采用、建议或需确认")

    payload = {
        "score": score,
        "decision": decision,
        "budget_cny": budget,
        "major_issues": major_issues,
        "minor_issues": minor_issues,
        "missing_fields": missing_fields,
        "ai_style_flags": ai_style_flags,
        "budget_method_warnings": budget_method_warnings,
        "uncertainty_as_fact_flags": uncertainty_flags,
        "hard_flags": hard_flags,
        "readiness": readiness,
        "recommendations": recommendations,
        "checks": checks,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if args.fail_below is not None and score < args.fail_below:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
