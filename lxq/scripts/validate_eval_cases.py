#!/usr/bin/env python3
"""Validate LXQ eval-case triplets, category counts, and rubric structure."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


REQUIRED_RUBRIC_KEYS = {
    "task_type", "invocation_intensity", "required_sections", "must_include",
    "must_not_include", "scoring", "pass_threshold",
}
SCORING_KEYS = {
    "innovation", "feasibility", "client_fit", "methodology",
    "evidence_integrity", "language_quality", "budget_fit", "risk_control",
}
EXPECTED_CATEGORIES = {
    "基金售前方向筛选": 10,
    "客户交付完整方案": 5,
    "生信方案": 5,
    "湿实验方案": 5,
    "文献精读": 3,
    "投稿返修": 2,
}
INTENSITIES = {"light", "standard", "strict", "forensic"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("eval_dir", type=Path)
    return parser.parse_args()


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1).strip() if match else ""


def main() -> int:
    args = parse_args()
    root = args.eval_dir.resolve()
    if not root.is_dir():
        print(json.dumps({"error": f"eval directory not found: {root}"}, ensure_ascii=False))
        return 2

    errors: list[str] = []
    categories: Counter[str] = Counter()
    stems = sorted({path.name[:8] for path in root.glob("case_*_input.md")})
    if len(stems) != 30:
        errors.append(f"expected 30 case stems, found {len(stems)}")

    for stem in stems:
        paths = {
            "input": root / f"{stem}_input.md",
            "expected": root / f"{stem}_expected.md",
            "rubric": root / f"{stem}_rubric.yaml",
        }
        for kind, path in paths.items():
            if not path.is_file():
                errors.append(f"{stem}: missing {kind} file")
        if any(not path.is_file() for path in paths.values()):
            continue

        input_text = paths["input"].read_text(encoding="utf-8")
        expected_text = paths["expected"].read_text(encoding="utf-8")
        rubric_text = paths["rubric"].read_text(encoding="utf-8")
        if len(input_text.strip()) < 80:
            errors.append(f"{stem}: input is too short")
        if len(expected_text.strip()) < 80:
            errors.append(f"{stem}: expected behavior is too short")

        present_keys = set(re.findall(r"(?m)^([a-z_]+):", rubric_text))
        missing_keys = REQUIRED_RUBRIC_KEYS - present_keys
        if missing_keys:
            errors.append(f"{stem}: rubric missing keys {sorted(missing_keys)}")

        task_type = scalar(rubric_text, "task_type")
        intensity = scalar(rubric_text, "invocation_intensity")
        categories[task_type] += 1
        if intensity not in INTENSITIES:
            errors.append(f"{stem}: invalid invocation_intensity '{intensity}'")
        if f"`{intensity}`" not in expected_text:
            errors.append(f"{stem}: expected file does not match rubric intensity")

        score_block = rubric_text.split("scoring:", 1)[1].split("pass_threshold:", 1)[0] if "scoring:" in rubric_text and "pass_threshold:" in rubric_text else ""
        scores = {
            name: int(value)
            for name, value in re.findall(r"(?m)^\s{2}([a-z_]+):\s*(\d+)\s*$", score_block)
        }
        if set(scores) != SCORING_KEYS:
            errors.append(f"{stem}: scoring keys mismatch")
        elif sum(scores.values()) != 100:
            errors.append(f"{stem}: scoring weights total {sum(scores.values())}, expected 100")
        threshold = scalar(rubric_text, "pass_threshold")
        if not threshold.isdigit() or not 0 <= int(threshold) <= 100:
            errors.append(f"{stem}: invalid pass_threshold '{threshold}'")

    if dict(categories) != EXPECTED_CATEGORIES:
        errors.append(f"category counts mismatch: {dict(categories)}")

    payload = {
        "cases": len(stems),
        "files": len(list(root.glob("case_*"))),
        "categories": dict(categories),
        "errors": errors,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
