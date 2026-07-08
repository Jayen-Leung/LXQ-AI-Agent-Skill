#!/usr/bin/env python3
"""Create a profile-aware, auditable LXQ review bundle without overwriting files."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path


ISSUE_FIELDS = [
    "id", "severity", "domain", "artifact", "location", "finding",
    "evidence", "impact", "required_action", "status", "verification",
    "source_class", "owner", "author_input_needed",
]
EVIDENCE_FIELDS = [
    "claim_id", "exact_claim", "claim_type", "source_data", "analysis",
    "result_artifact", "display_artifact", "manuscript_location",
    "citation_status", "availability_location", "support", "boundary",
    "limitation", "required_change",
]
TERM_FIELDS = [
    "term_id", "canonical_term", "variants_found", "definition",
    "unit_or_format", "first_use", "applies_to", "status", "notes",
]
CHANGE_FIELDS = [
    "change_id", "artifact", "location", "change_type", "before", "after",
    "rationale", "evidence", "meaning_changed", "author_confirmation",
    "verification",
]
RESPONSE_FIELDS = [
    "comment_id", "source", "verbatim_or_faithful_comment", "category",
    "severity", "proposed_action", "evidence_needed", "manuscript_location",
    "owner", "status", "verification",
]
AVAILABILITY_FIELDS = [
    "dataset_id", "description", "supports_claims", "data_state",
    "access_route", "repository", "identifier", "version",
    "license_or_terms", "restriction_reason", "access_process",
    "metadata_status", "status", "verification",
]
GRANT_REQUIREMENT_FIELDS = [
    "requirement_id", "source", "official_requirement", "category",
    "proposal_location", "status", "owner", "verification",
]
GRANT_AIM_FIELDS = [
    "aim_id", "question_or_hypothesis", "rationale", "preliminary_evidence",
    "design", "experimental_unit", "primary_outcome", "analysis",
    "success_criterion", "dependency", "risk", "alternative", "deliverable",
    "milestone", "owner", "timing", "budget_link", "status",
]
GRANT_STUDY_FIELDS = [
    "component_id", "aim_id", "research_object", "setting", "study_design",
    "experimental_unit", "sample_size", "sample_size_basis",
    "groups_and_controls", "inclusion_criteria", "exclusion_criteria",
    "primary_endpoint", "secondary_endpoints", "timepoints",
    "biospecimens_or_data", "detection_indicators", "wet_lab_methods",
    "data_source", "bioinformatics_algorithms", "validation_strategy",
    "statistical_methods", "missing_data_and_multiplicity", "planned_visuals",
    "expected_result", "success_criterion", "budget_link", "status", "notes",
]
LITERATURE_EVIDENCE_FIELDS = [
    "paper_id", "citation", "doi_or_id", "article_type", "review_question",
    "population_or_model", "design", "sample_size", "exposure_or_intervention",
    "comparator", "outcome", "effect_and_uncertainty", "main_claim",
    "support_grade", "bias_or_limitation", "source_anchor", "full_text_status",
    "notes",
]
LITERATURE_FILE_FIELDS = [
    "paper_id", "title", "doi", "pmid", "pmcid", "arxiv_id", "version",
    "source_url", "access_route", "license_or_status", "retrieved_date",
    "filename", "size_bytes", "sha256", "identity_verified", "notes",
]
PROFILES = {"core", "revision", "submission", "full", "grant", "literature", "complete"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New or empty output directory")
    parser.add_argument("--title", default="LXQ research quality-control review")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="core")
    return parser.parse_args()


def write_tsv(path: Path, fields: list[str]) -> None:
    with path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()


def planned_files(output: Path, profile: str) -> list[Path]:
    planned = [
        output / "scope.json", output / "issue-register.tsv",
        output / "evidence-map.tsv", output / "terminology-ledger.tsv",
        output / "change-log.tsv", output / "qc-report.md",
    ]
    if profile in {"revision", "full", "complete"}:
        planned.append(output / "reviewer-response-tracker.tsv")
    if profile in {"submission", "full", "complete"}:
        planned.append(output / "availability-inventory.tsv")
    if profile in {"grant", "complete"}:
        planned.extend([
            output / "funding-requirements.tsv", output / "grant-aims.tsv",
            output / "grant-study-design.tsv", output / "customer-scheme.md",
        ])
    if profile in {"literature", "complete"}:
        planned.extend([output / "literature-evidence.tsv", output / "literature-files.tsv"])
    return planned


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    planned = planned_files(output, args.profile)
    existing = [path for path in planned if path.exists()]
    if existing:
        names = ", ".join(path.name for path in existing)
        raise SystemExit(f"Refusing to overwrite existing review files: {names}")

    scope = {
        "schema_version": "2.3",
        "review_date": date.today().isoformat(),
        "title": args.title,
        "profile": args.profile,
        "invocation_intensity": "",
        "task_modes": [],
        "artifact_tracks": [],
        "scientific_question": "",
        "study_design": "",
        "endpoint_or_estimand": "",
        "cohort": "",
        "assay": "",
        "reference_or_build": "",
        "core_claim": "",
        "evidence_boundary": "",
        "intended_use": "",
        "primary_reader": "",
        "target_journal": "",
        "client_background": "",
        "funding_scheme": "",
        "funding_call_source": "",
        "project_duration": "",
        "budget_ceiling": "",
        "artifacts_available": [],
        "artifacts_unavailable_or_not_reviewed": [],
        "review_boundary": "",
        "decision": "",
        "package_readiness": "",
    }
    (output / "scope.json").write_text(
        json.dumps(scope, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_tsv(output / "issue-register.tsv", ISSUE_FIELDS)
    write_tsv(output / "evidence-map.tsv", EVIDENCE_FIELDS)
    write_tsv(output / "terminology-ledger.tsv", TERM_FIELDS)
    write_tsv(output / "change-log.tsv", CHANGE_FIELDS)
    if args.profile in {"revision", "full", "complete"}:
        write_tsv(output / "reviewer-response-tracker.tsv", RESPONSE_FIELDS)
    if args.profile in {"submission", "full", "complete"}:
        write_tsv(output / "availability-inventory.tsv", AVAILABILITY_FIELDS)
    if args.profile in {"grant", "complete"}:
        write_tsv(output / "funding-requirements.tsv", GRANT_REQUIREMENT_FIELDS)
        write_tsv(output / "grant-aims.tsv", GRANT_AIM_FIELDS)
        write_tsv(output / "grant-study-design.tsv", GRANT_STUDY_FIELDS)
        customer_scheme = """# 医学科研项目客户交付方案

> 说明：将不确定信息标注为“建议”“拟采用”“计划”“需进一步确认”或 LXQ 占位符；不得把计划或假设写成既定事实。

## 一、拟定题目

## 二、研究背景与临床问题

## 三、研究假说

## 四、研究目标

## 五、主要研究内容

## 六、拟解决的关键问题

## 七、研究对象与样本量

## 八、分组、检测指标与随访节点

## 九、统计学与模型构建

## 十、技术路线

### 湿实验方案

### 生信方案

## 十一、创新点

## 十二、可行性分析

## 十三、风险与替代方案

## 十四、预期成果

## 参考文献
"""
        (output / "customer-scheme.md").write_text(customer_scheme, encoding="utf-8")
    if args.profile in {"literature", "complete"}:
        write_tsv(output / "literature-evidence.tsv", LITERATURE_EVIDENCE_FIELDS)
        write_tsv(output / "literature-files.tsv", LITERATURE_FILE_FIELDS)

    report = f"""# {args.title}

## Scope and fact base

- Task modes and artifact tracks:
- Invocation intensity:
- Scientific question and intended use:
- Core claim, evidence, and boundary:
- Artifacts reviewed:
- Artifacts unavailable or not reviewed:
- Review date and environment: {date.today().isoformat()}

## Decision

`PASS`, `CONDITIONAL PASS`, or `FAIL`

## Package readiness

`ready_to_use`, `conditional`, `needs_author_input`, or `blocked`

## Executive findings

## Evidence and provenance

## Issue summary

## Terminology and identifier consistency

## Changes performed

## Revision and availability status

## Grant, customer-delivery, and literature status

## Verification performed

## Remaining limitations and owner actions

## Reproducibility handoff
"""
    (output / "qc-report.md").write_text(report, encoding="utf-8")
    print(f"Created LXQ {args.profile} review bundle in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
