#!/usr/bin/env python3
"""Validate the file set and table schemas of an LXQ review bundle."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SCHEMAS = {
    "issue-register.tsv": [
        "id", "severity", "domain", "artifact", "location", "finding",
        "evidence", "impact", "required_action", "status", "verification",
    ],
    "evidence-map.tsv": [
        "claim_id", "exact_claim", "claim_type", "source_data", "analysis",
        "result_artifact", "display_artifact", "manuscript_location",
        "citation_status", "availability_location", "support", "boundary",
        "limitation", "required_change",
    ],
    "terminology-ledger.tsv": [
        "term_id", "canonical_term", "variants_found", "definition",
        "unit_or_format", "first_use", "applies_to", "status", "notes",
    ],
    "change-log.tsv": [
        "change_id", "artifact", "location", "change_type", "before", "after",
        "rationale", "evidence", "meaning_changed", "author_confirmation",
        "verification",
    ],
    "reviewer-response-tracker.tsv": [
        "comment_id", "source", "verbatim_or_faithful_comment", "category",
        "severity", "proposed_action", "evidence_needed", "manuscript_location",
        "owner", "status", "verification",
    ],
    "availability-inventory.tsv": [
        "dataset_id", "description", "supports_claims", "data_state",
        "access_route", "repository", "identifier", "version",
        "license_or_terms", "restriction_reason", "access_process",
        "metadata_status", "status", "verification",
    ],
    "funding-requirements.tsv": [
        "requirement_id", "source", "official_requirement", "category",
        "proposal_location", "status", "owner", "verification",
    ],
    "grant-aims.tsv": [
        "aim_id", "question_or_hypothesis", "rationale", "preliminary_evidence",
        "design", "experimental_unit", "primary_outcome", "analysis",
        "success_criterion", "dependency", "risk", "alternative", "deliverable",
        "milestone", "owner", "timing", "budget_link", "status",
    ],
    "grant-study-design.tsv": [
        "component_id", "aim_id", "research_object", "setting", "study_design",
        "experimental_unit", "sample_size", "sample_size_basis",
        "groups_and_controls", "inclusion_criteria", "exclusion_criteria",
        "primary_endpoint", "secondary_endpoints", "timepoints",
        "biospecimens_or_data", "detection_indicators", "wet_lab_methods",
        "data_source", "bioinformatics_algorithms", "validation_strategy",
        "statistical_methods", "missing_data_and_multiplicity", "planned_visuals",
        "expected_result", "success_criterion", "budget_link", "status", "notes",
    ],
    "literature-evidence.tsv": [
        "paper_id", "citation", "doi_or_id", "article_type", "review_question",
        "population_or_model", "design", "sample_size", "exposure_or_intervention",
        "comparator", "outcome", "effect_and_uncertainty", "main_claim",
        "support_grade", "bias_or_limitation", "source_anchor", "full_text_status",
        "notes",
    ],
    "literature-files.tsv": [
        "paper_id", "title", "doi", "pmid", "pmcid", "arxiv_id", "version",
        "source_url", "access_route", "license_or_status", "retrieved_date",
        "filename", "size_bytes", "sha256", "identity_verified", "notes",
    ],
}
BASE_FILES = {
    "scope.json", "issue-register.tsv", "evidence-map.tsv",
    "terminology-ledger.tsv", "change-log.tsv", "qc-report.md",
}
READINESS = {"", "ready_to_use", "conditional", "needs_author_input", "blocked"}
DECISIONS = {"", "PASS", "CONDITIONAL PASS", "FAIL"}
INTENSITIES = {"", "light", "standard", "strict", "forensic"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    parser.add_argument(
        "--profile", choices=["core", "revision", "submission", "full", "grant", "literature", "complete"],
        default=None, help="Expected profile; defaults to scope.json",
    )
    return parser.parse_args()


def read_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return next(csv.reader(handle, delimiter="\t"), [])


def main() -> int:
    args = parse_args()
    bundle = args.bundle.resolve()
    errors: list[str] = []
    if not bundle.is_dir():
        print(f"ERROR: bundle directory does not exist: {bundle}")
        return 2

    scope_path = bundle / "scope.json"
    scope: dict[str, object] = {}
    if scope_path.is_file():
        try:
            payload = json.loads(scope_path.read_text(encoding="utf-8-sig"))
            if not isinstance(payload, dict):
                errors.append("scope.json must contain a JSON object")
            else:
                scope = payload
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid scope.json: {exc}")
    profile = args.profile or str(scope.get("profile", "core"))
    if profile not in {"core", "revision", "submission", "full", "grant", "literature", "complete"}:
        errors.append(f"invalid profile '{profile}'")
        profile = "core"

    required = set(BASE_FILES)
    if profile in {"revision", "full", "complete"}:
        required.add("reviewer-response-tracker.tsv")
    if profile in {"submission", "full", "complete"}:
        required.add("availability-inventory.tsv")
    if profile in {"grant", "complete"}:
        required.update({
            "funding-requirements.tsv", "grant-aims.tsv",
            "grant-study-design.tsv", "customer-scheme.md",
        })
    if profile in {"literature", "complete"}:
        required.update({"literature-evidence.tsv", "literature-files.tsv"})
    for name in sorted(required):
        if not (bundle / name).is_file():
            errors.append(f"missing required file: {name}")

    if scope:
        if str(scope.get("schema_version", "")) not in {"2.0", "2.1", "2.2", "2.3"}:
            errors.append("scope.json schema_version must be '2.0', '2.1', '2.2', or '2.3'")
        if str(scope.get("invocation_intensity", "")) not in INTENSITIES:
            errors.append("scope.json has invalid invocation_intensity")
        if str(scope.get("decision", "")) not in DECISIONS:
            errors.append("scope.json has invalid decision")
        if str(scope.get("package_readiness", "")) not in READINESS:
            errors.append("scope.json has invalid package_readiness")

    for name, expected in SCHEMAS.items():
        path = bundle / name
        if not path.is_file():
            continue
        header = read_header(path)
        missing = [field for field in expected if field not in header]
        if missing:
            errors.append(f"{name} missing columns: {', '.join(missing)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Bundle validation failed with {len(errors)} error(s)")
        return 2
    print(f"Valid LXQ {profile} review bundle: {bundle}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
