#!/usr/bin/env python3
"""Validate an LXQ issue register and optionally fail on unresolved severity."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


REQUIRED = [
    "id", "severity", "domain", "artifact", "location", "finding",
    "evidence", "impact", "required_action", "status", "verification",
]
SEVERITIES = {"blocker": 3, "major": 2, "minor": 1}
STATUSES = {"open", "resolved", "waived", "not-applicable"}
SOURCE_CLASSES = {"supplied-fact", "directly-verified", "inference", "assumption", "unresolved"}
YES_NO = {"yes", "no"}
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9-]*-\d{3,}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path, help="Issue register in .tsv, .csv, or .json")
    parser.add_argument(
        "--fail-on", choices=["none", "blocker", "major", "minor"],
        default="blocker", help="Exit 3 when an open issue reaches this severity",
    )
    return parser.parse_args()


def load_rows(path: Path) -> tuple[list[str], list[dict[str, object]]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        rows = payload.get("issues") if isinstance(payload, dict) else payload
        if not isinstance(rows, list):
            raise ValueError("JSON must be a list or an object with an 'issues' list")
        fields = sorted({key for row in rows if isinstance(row, dict) for key in row})
        return fields, rows
    if suffix not in {".tsv", ".csv"}:
        raise ValueError("Register must end in .tsv, .csv, or .json")
    delimiter = "\t" if suffix == ".tsv" else ","
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    args = parse_args()
    if not args.register.is_file():
        print(f"ERROR: register does not exist: {args.register}")
        return 2
    try:
        fields, rows = load_rows(args.register)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 2

    errors: list[str] = []
    missing = [field for field in REQUIRED if field not in fields]
    if missing:
        errors.append("missing required columns: " + ", ".join(missing))

    seen: set[str] = set()
    unresolved: list[tuple[str, str]] = []
    for number, row in enumerate(rows, start=2):
        if not isinstance(row, dict):
            errors.append(f"row {number}: must be an object")
            continue
        issue_id = str(row.get("id", "")).strip()
        severity = str(row.get("severity", "")).strip().lower()
        status = str(row.get("status", "")).strip().lower()
        if not ID_PATTERN.match(issue_id):
            errors.append(f"row {number}: invalid id '{issue_id}'")
        if issue_id in seen:
            errors.append(f"row {number}: duplicate id '{issue_id}'")
        seen.add(issue_id)
        if severity not in SEVERITIES:
            errors.append(f"row {number}: invalid severity '{row.get('severity', '')}'")
        if status not in STATUSES:
            errors.append(f"row {number}: invalid status '{row.get('status', '')}'")
        for field in ("domain", "artifact", "finding", "impact", "required_action"):
            if not str(row.get(field, "")).strip():
                errors.append(f"row {number}: '{field}' is empty")
        if status == "waived" and not str(row.get("verification", "")).strip():
            errors.append(f"row {number}: waived issue lacks waiver rationale in verification")
        source_class = str(row.get("source_class", "")).strip().lower()
        if "source_class" in fields and source_class and source_class not in SOURCE_CLASSES:
            errors.append(f"row {number}: invalid source_class '{row.get('source_class', '')}'")
        author_input = str(row.get("author_input_needed", "")).strip().lower()
        if "author_input_needed" in fields and author_input and author_input not in YES_NO:
            errors.append(
                f"row {number}: author_input_needed must be yes/no, got '{row.get('author_input_needed', '')}'"
            )
        if severity in SEVERITIES and status == "open":
            unresolved.append((issue_id, severity))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s)")
        return 2

    counts = {name: 0 for name in SEVERITIES}
    for _, severity in unresolved:
        counts[severity] += 1
    print(
        f"Valid register: {len(rows)} issue(s); unresolved "
        f"Blocker={counts['blocker']}, Major={counts['major']}, Minor={counts['minor']}"
    )
    if args.fail_on != "none":
        threshold = SEVERITIES[args.fail_on]
        failing = [issue_id for issue_id, severity in unresolved if SEVERITIES[severity] >= threshold]
        if failing:
            print("FAIL-ON threshold met by: " + ", ".join(failing))
            return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
