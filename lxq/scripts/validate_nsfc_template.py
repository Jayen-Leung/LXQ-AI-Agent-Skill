#!/usr/bin/env python3
"""Validate the structural layout contract of an LXQ NSFC formal DOCX."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
W = "{%s}" % NS["w"]

REQUIRED_TEXT = [
    "2026年度国家自然科学基金",
    "正式申报书",
    "专家评审意见表",
    "基本情况表",
    "项目摘要（限400字）",
    "报告正文",
    "（一）立项依据与研究内容（建议8000字以下）：",
    "1．项目的立项依据（研究意义、国内外研究现状及发展动态分析，需结合科学研究发展趋势来论述科学意义；或结合国民经济和社会发展中迫切需要解决的关键科技问题来论述其应用前景。附主要参考文献目录）；",
    "2．项目的研究内容、研究目标，以及拟解决的关键科学问题（此部分为重点阐述内容）；",
    "3．拟采取的研究方案及可行性分析（包括研究方法、技术路线、实验手段、关键技术等说明）；",
    "4．本项目的特色与创新之处；",
    "5．年度研究计划及预期研究结果（包括拟组织的重要学术交流活动、国际合作与交流计划等）。",
    "（二）研究基础（与本项目相关的研究工作积累和已取得的研究工作成绩）；",
    "申请人简历（依照国自然申报书个人简历格式填写）",
    "近五年主持的国家级科研项目",
    "近五年代表性论著（限5篇）",
    "其他除论著外代表性成果（限5项）",
]

EXPECTED_LAYOUT = {
    "pgSz": {"w": 11906, "h": 16838},
    "pgMar": {
        "top": 1440,
        "right": 1069,
        "bottom": 918,
        "left": 1177,
        "header": 851,
        "footer": 992,
    },
}

UNRESOLVED = (
    "[AUTHOR_INPUT_NEEDED",
    "[EVIDENCE_NEEDED",
    "[POLICY_CHECK_NEEDED",
    "[EXPERT_CONFIRMATION_NEEDED",
    "需进一步确认",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="NSFC formal application DOCX")
    parser.add_argument(
        "--allow-unresolved",
        action="store_true",
        help="Permit visible LXQ placeholders in a draft",
    )
    return parser.parse_args()


def paragraph_texts(root: ET.Element) -> list[str]:
    texts: list[str] = []
    for paragraph in root.findall(".//w:p", NS):
        text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS)).strip()
        if text:
            texts.append(text)
    return texts


def int_attr(element: ET.Element, name: str) -> int | None:
    value = element.get(W + name)
    return None if value is None else int(value)


def main() -> int:
    args = parse_args()
    path = args.document.resolve()
    errors: list[str] = []

    if not path.is_file():
        print(f"ERROR: document does not exist: {path}")
        return 2
    if path.suffix.lower() != ".docx":
        print("ERROR: formal NSFC delivery must be a .docx file")
        return 2

    try:
        with zipfile.ZipFile(path) as archive:
            document_xml = archive.read("word/document.xml")
            names = set(archive.namelist())
            footer_xml = "\n".join(
                archive.read(name).decode("utf-8", errors="replace")
                for name in names
                if re.fullmatch(r"word/footer\d+\.xml", name)
            )
    except (zipfile.BadZipFile, KeyError) as exc:
        print(f"ERROR: invalid DOCX package: {exc}")
        return 2

    root = ET.fromstring(document_xml)
    texts = paragraph_texts(root)
    joined = "\n".join(texts)

    positions: list[int] = []
    for label in REQUIRED_TEXT:
        try:
            positions.append(texts.index(label))
        except ValueError:
            errors.append(f"missing required template text: {label}")
    if len(positions) == len(REQUIRED_TEXT) and positions != sorted(positions):
        errors.append("required template sections are out of order")

    tables = root.findall(".//w:tbl", NS)
    if len(tables) < 3:
        errors.append(f"expected at least 3 template tables, found {len(tables)}")

    sect_pr = root.find(".//w:sectPr", NS)
    if sect_pr is None:
        errors.append("missing section page layout")
    else:
        for element_name, expected in EXPECTED_LAYOUT.items():
            element = sect_pr.find(f"w:{element_name}", NS)
            if element is None:
                errors.append(f"missing section element: {element_name}")
                continue
            for attr, expected_value in expected.items():
                actual = int_attr(element, attr)
                if actual is None or abs(actual - expected_value) > 5:
                    errors.append(
                        f"layout mismatch {element_name}.{attr}: expected {expected_value}, found {actual}"
                    )

    if "PAGE" not in footer_xml:
        errors.append("missing PAGE field in footer")

    if not args.allow_unresolved:
        found = [marker for marker in UNRESOLVED if marker in joined]
        if found:
            errors.append("unresolved markers remain: " + ", ".join(found))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"NSFC template validation failed with {len(errors)} error(s)")
        return 2

    print(
        f"Valid LXQ NSFC formal DOCX: {path}; "
        f"required sections={len(REQUIRED_TEXT)}; tables={len(tables)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
