#!/usr/bin/env python3
"""Validate a customer-facing LXQ medical research grant delivery bundle."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


DESIGN_FILE = "grant-study-design.tsv"
SCHEME_FILE = "customer-scheme.md"
REQUIRED_COLUMNS = [
    "component_id", "aim_id", "research_object", "setting", "study_design",
    "experimental_unit", "sample_size", "sample_size_basis",
    "groups_and_controls", "inclusion_criteria", "exclusion_criteria",
    "primary_endpoint", "secondary_endpoints", "timepoints",
    "biospecimens_or_data", "detection_indicators", "wet_lab_methods",
    "data_source", "bioinformatics_algorithms", "validation_strategy",
    "statistical_methods", "missing_data_and_multiplicity", "planned_visuals",
    "expected_result", "success_criterion", "budget_link", "status", "notes",
]
FINAL_REQUIRED = [
    "component_id", "research_object", "setting", "study_design",
    "experimental_unit", "sample_size", "sample_size_basis",
    "groups_and_controls", "inclusion_criteria", "exclusion_criteria",
    "primary_endpoint", "secondary_endpoints", "timepoints",
    "biospecimens_or_data", "detection_indicators", "wet_lab_methods",
    "data_source", "bioinformatics_algorithms", "validation_strategy",
    "statistical_methods", "missing_data_and_multiplicity", "planned_visuals",
    "expected_result", "success_criterion", "budget_link", "status",
]
SECTION_LABELS_ZH = [
    "一、拟定题目",
    "二、研究背景与临床问题",
    "三、研究假说",
    "四、研究目标",
    "五、主要研究内容",
    "六、拟解决的关键问题",
    "七、研究对象与样本量",
    "八、分组、检测指标与随访节点",
    "九、统计学与模型构建",
    "十、技术路线",
    "十一、创新点",
    "十二、可行性分析",
    "十三、风险与替代方案",
    "十四、预期成果",
    "参考文献",
]
SECTION_LABELS_EN = [
    "Proposed title",
    "Research background and rationale",
    "Research objectives",
    "Main research content",
    "Key questions to resolve",
    "Technical route and methodological design",
    "Sample size and study population",
    "Statistics and model development",
    "Innovation",
    "Feasibility",
    "Expected outputs",
    "References",
]
UNRESOLVED_MARKERS = (
    "[AUTHOR_INPUT_NEEDED", "[EVIDENCE_NEEDED", "[POLICY_CHECK_NEEDED",
    "[EXPERT_CONFIRMATION_NEEDED", "需进一步确认",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path, help="LXQ grant or complete bundle")
    parser.add_argument(
        "--language", choices=["zh", "en"], default="zh",
        help="Expected customer-scheme heading language; defaults to zh",
    )
    parser.add_argument(
        "--allow-empty", action="store_true",
        help="Check only files, columns, and section structure for a fresh scaffold",
    )
    parser.add_argument(
        "--allow-unresolved", action="store_true",
        help="Permit visible unresolved markers for a draft delivery",
    )
    return parser.parse_args()


def read_design(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def scheme_sections(text: str, labels: list[str]) -> tuple[list[tuple[str, int]], list[str]]:
    headings: list[tuple[str, int]] = []
    errors: list[str] = []
    lines = text.splitlines()
    for label in labels:
        matches = [
            index for index, line in enumerate(lines)
            if re.match(r"^#{1,6}\s+", line) and label in line
        ]
        if len(matches) != 1:
            errors.append(f"{SCHEME_FILE}: expected one heading containing '{label}', found {len(matches)}")
        else:
            headings.append((label, matches[0]))
    if len(headings) == len(labels):
        positions = [position for _, position in headings]
        if positions != sorted(positions):
            errors.append(f"{SCHEME_FILE}: required sections are out of order")
    return headings, errors


def section_has_content(lines: list[str], start: int, end: int) -> bool:
    for line in lines[start + 1:end]:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and not stripped.startswith("> 说明："):
            return True
    return False


def main() -> int:
    args = parse_args()
    bundle = args.bundle.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not bundle.is_dir():
        print(f"ERROR: bundle directory does not exist: {bundle}")
        return 2

    design_path = bundle / DESIGN_FILE
    scheme_path = bundle / SCHEME_FILE
    for path in (design_path, scheme_path):
        if not path.is_file():
            errors.append(f"missing required file: {path.name}")

    rows: list[dict[str, str]] = []
    if design_path.is_file():
        header, rows = read_design(design_path)
        missing = [field for field in REQUIRED_COLUMNS if field not in header]
        if missing:
            errors.append(f"{DESIGN_FILE} missing columns: {', '.join(missing)}")
        if not rows and not args.allow_empty:
            errors.append(f"{DESIGN_FILE}: at least one study-design row is required")

        seen: set[str] = set()
        for row_number, row in enumerate(rows, start=2):
            component_id = (row.get("component_id") or "").strip()
            if component_id and component_id in seen:
                errors.append(f"{DESIGN_FILE} row {row_number}: duplicate component_id '{component_id}'")
            seen.add(component_id)
            if not args.allow_empty:
                empty = [field for field in FINAL_REQUIRED if not (row.get(field) or "").strip()]
                if empty:
                    errors.append(
                        f"{DESIGN_FILE} row {row_number}: empty completion fields: {', '.join(empty)}"
                    )
                unresolved = [
                    field for field in FINAL_REQUIRED
                    if any(marker in (row.get(field) or "") for marker in UNRESOLVED_MARKERS)
                ]
                if unresolved and not args.allow_unresolved:
                    errors.append(
                        f"{DESIGN_FILE} row {row_number}: unresolved completion fields: {', '.join(unresolved)}"
                    )

    if scheme_path.is_file():
        text = scheme_path.read_text(encoding="utf-8-sig")
        substantive_text = "\n".join(
            line for line in text.splitlines() if not line.lstrip().startswith("> 说明：")
        )
        labels = SECTION_LABELS_ZH if args.language == "zh" else SECTION_LABELS_EN
        headings, heading_errors = scheme_sections(text, labels)
        errors.extend(heading_errors)
        if not args.allow_empty and len(headings) == len(labels):
            lines = text.splitlines()
            for index, (label, start) in enumerate(headings):
                end = headings[index + 1][1] if index + 1 < len(headings) else len(lines)
                if not section_has_content(lines, start, end):
                    errors.append(f"{SCHEME_FILE}: section '{label}' has no substantive content")
        if not args.allow_unresolved:
            found = [marker for marker in UNRESOLVED_MARKERS if marker in substantive_text]
            if found and not args.allow_empty:
                errors.append(f"{SCHEME_FILE}: unresolved markers remain: {', '.join(found)}")
        if re.search(r"(?:\bfirst\b|首次|首创|填补空白)", substantive_text, flags=re.IGNORECASE):
            warnings.append(
                f"{SCHEME_FILE}: verify any priority or novelty claim against the closest literature"
            )

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Grant delivery validation failed with {len(errors)} error(s)")
        return 2

    mode = "scaffold structure" if args.allow_empty else "completed delivery"
    print(f"Valid LXQ grant {mode}: {bundle}; language={args.language}; design rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
