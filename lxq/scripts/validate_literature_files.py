#!/usr/bin/env python3
"""Validate an LXQ literature file manifest and verify local file hashes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


REQUIRED = [
    "paper_id", "title", "doi", "pmid", "pmcid", "arxiv_id", "version",
    "source_url", "access_route", "license_or_status", "retrieved_date",
    "filename", "size_bytes", "sha256", "identity_verified", "notes",
]
ACCESS_ROUTES = {
    "user-provided", "institution-authorized", "publisher-open-access",
    "pubmed-central", "preprint-repository", "institutional-repository",
    "library-document-delivery", "metadata-only",
}
YES_NO = {"yes", "no"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="literature-files.tsv")
    parser.add_argument(
        "--files-root", type=Path, default=None,
        help="Root for relative filenames; defaults to the manifest directory",
    )
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    manifest = args.manifest.resolve()
    if not manifest.is_file():
        print(f"ERROR: manifest does not exist: {manifest}")
        return 2
    root = (args.files_root or manifest.parent).resolve()
    errors: list[str] = []
    seen: set[str] = set()

    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = list(reader.fieldnames or [])
        missing = [field for field in REQUIRED if field not in fields]
        if missing:
            print("ERROR: missing required columns: " + ", ".join(missing))
            return 2
        rows = list(reader)

    for number, row in enumerate(rows, start=2):
        paper_id = row["paper_id"].strip()
        if not paper_id:
            errors.append(f"row {number}: paper_id is empty")
        elif paper_id in seen:
            errors.append(f"row {number}: duplicate paper_id '{paper_id}'")
        seen.add(paper_id)

        route = row["access_route"].strip().lower()
        if route and route not in ACCESS_ROUTES:
            errors.append(f"row {number}: invalid access_route '{row['access_route']}'")
        verified = row["identity_verified"].strip().lower()
        if verified and verified not in YES_NO:
            errors.append(f"row {number}: identity_verified must be yes/no")

        filename = row["filename"].strip()
        if not filename:
            if route and route != "metadata-only":
                errors.append(f"row {number}: non-metadata route lacks filename")
            continue
        candidate = (root / filename).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            errors.append(f"row {number}: filename escapes files root")
            continue
        if not candidate.is_file():
            errors.append(f"row {number}: file not found '{filename}'")
            continue

        with candidate.open("rb") as source:
            prefix = source.read(512)
        if b"<html" in prefix.lower() or b"<!doctype html" in prefix.lower():
            errors.append(f"row {number}: '{filename}' appears to be HTML, not full text")
        if candidate.suffix.lower() == ".pdf" and not prefix.startswith(b"%PDF-"):
            errors.append(f"row {number}: '{filename}' lacks a PDF file signature")

        size_text = row["size_bytes"].strip()
        if size_text:
            try:
                expected_size = int(size_text)
                if expected_size != candidate.stat().st_size:
                    errors.append(f"row {number}: size mismatch for '{filename}'")
            except ValueError:
                errors.append(f"row {number}: size_bytes is not an integer")
        hash_text = row["sha256"].strip()
        if hash_text:
            if not SHA256_RE.match(hash_text):
                errors.append(f"row {number}: invalid SHA-256 format")
            elif sha256(candidate).lower() != hash_text.lower():
                errors.append(f"row {number}: SHA-256 mismatch for '{filename}'")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Literature manifest validation failed with {len(errors)} error(s)")
        return 2
    print(f"Valid literature manifest: {len(rows)} record(s); files root={root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
