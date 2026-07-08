#!/usr/bin/env python3
"""Create a deterministic provenance manifest for a research project tree."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


DEFAULT_EXTENSIONS = {
    ".bam", ".bed", ".bib", ".bim", ".bgen", ".cif", ".cram", ".csv",
    ".docx", ".enw", ".fasta", ".fastq", ".fa", ".fq", ".gff", ".gff3",
    ".gtf", ".h5", ".h5ad", ".html", ".ipynb", ".json", ".loom", ".md",
    ".mtx", ".nbib", ".nii", ".nii.gz", ".parquet", ".pdf", ".ped", ".png",
    ".pptx", ".py", ".r", ".rds", ".ris", ".Rmd", ".sam", ".sh", ".svg",
    ".tif", ".tiff", ".tsv", ".txt", ".vcf", ".vcf.gz", ".xlsx", ".yaml", ".yml",
}


def compound_suffix(path: Path) -> str:
    name = path.name.lower()
    for suffix in (".nii.gz", ".vcf.gz"):
        if name.endswith(suffix):
            return suffix
    return path.suffix.lower()


def sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path, extensions: set[str], output: Path) -> Iterable[Path]:
    output_resolved = output.resolve()
    for path in sorted(root.rglob("*"), key=lambda p: p.as_posix().lower()):
        if path.is_symlink() or not path.is_file():
            continue
        if path.resolve() == output_resolved:
            continue
        if extensions and compound_suffix(path) not in extensions:
            continue
        yield path


def build_record(path: Path, root: Path, include_hash: bool) -> dict[str, object]:
    stat = path.stat()
    record: dict[str, object] = {
        "path": path.relative_to(root).as_posix(),
        "extension": compound_suffix(path),
        "size_bytes": stat.st_size,
        "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
    }
    if include_hash:
        record["sha256"] = sha256(path)
    return record


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Project directory to inventory")
    parser.add_argument("--output", type=Path, required=True, help="Output .json or .tsv file")
    parser.add_argument("--hash", action="store_true", help="Calculate SHA-256 checksums")
    parser.add_argument(
        "--all-files", action="store_true",
        help="Include all file extensions instead of the biomedical/research defaults",
    )
    parser.add_argument(
        "--extensions", nargs="*", default=None,
        help="Override extensions, for example: --extensions .fastq .vcf.gz .csv",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    if not root.is_dir():
        raise SystemExit(f"Project directory does not exist: {root}")
    if output.suffix.lower() not in {".json", ".tsv"}:
        raise SystemExit("--output must end in .json or .tsv")

    if args.all_files:
        extensions: set[str] = set()
    elif args.extensions is not None:
        extensions = {e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.extensions}
    else:
        extensions = {e.lower() for e in DEFAULT_EXTENSIONS}

    records = [build_record(path, root, args.hash) for path in iter_files(root, extensions, output)]
    output.parent.mkdir(parents=True, exist_ok=True)

    if output.suffix.lower() == ".json":
        payload = {
            "schema_version": "1.0",
            "root": str(root),
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "hash_algorithm": "sha256" if args.hash else None,
            "file_count": len(records),
            "files": records,
        }
        output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        fields = ["path", "extension", "size_bytes", "modified_utc"]
        if args.hash:
            fields.append("sha256")
        with output.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(records)

    print(f"Wrote {len(records)} records to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
