#!/usr/bin/env python3
"""Run dependency-free structural and smoke tests for the LXQ repository."""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "lxq"
EXPECTED_SCRIPTS = {
    "build_manifest.py",
    "generate_eval_cases.py",
    "scaffold_review.py",
    "score_delivery_quality.py",
    "score_grant_quality.py",
    "validate_eval_cases.py",
    "validate_grant_delivery.py",
    "validate_issue_register.py",
    "validate_literature_files.py",
    "validate_nsfc_template.py",
    "validate_review_bundle.py",
}
EXPECTED_SPECIALISTS = {
    "nature-writing", "nature-polishing", "nature-figure", "nature-response",
    "nature-citation", "nature-academic-search", "nature-reader", "nature-data",
    "nature-reviewer",
}
EXPECTED_CATALOGS = {
    "gptomics-bioskills": 562,
    "orchestra-ai-research-skills": 98,
}
EXPECTED_MANUSCRIPT_CONTRACTS = {
    "structure-narrative.md",
    "evidence-story.md",
    "reporting-statistics.md",
    "visual-presentation.md",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def run(*args: str) -> None:
    completed = subprocess.run(
        [sys.executable, *args], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    if completed.returncode != 0:
        fail(f"command failed ({completed.returncode}): {' '.join(args)}\n{completed.stdout}")


def validate_frontmatter() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("lxq/SKILL.md lacks YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("lxq/SKILL.md has unclosed YAML frontmatter")
    frontmatter = parts[1]
    if not re.search(r"(?m)^name:\s*lxq\s*$", frontmatter):
        fail("SKILL.md name must be lxq")
    description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    if not description or len(description.group(1).strip()) < 40:
        fail("SKILL.md description is missing or too short")


def validate_manifest_paths() -> str:
    text = (SKILL / "manifest.yaml").read_text(encoding="utf-8")
    match = re.search(r"(?m)^version:\s*([^\s]+)\s*$", text)
    if not match:
        fail("manifest.yaml lacks version")
    paths = sorted(set(re.findall(r"(?:static|references)/[A-Za-z0-9_./-]+\.(?:md|yaml)", text)))
    if not paths:
        fail("manifest.yaml contains no routed paths")
    missing = [path for path in paths if not (SKILL / path).is_file()]
    if missing:
        fail("manifest routes to missing files: " + ", ".join(missing))
    return match.group(1)


def validate_text_and_scripts() -> None:
    text_suffixes = {".md", ".yaml", ".yml", ".py"}
    for path in SKILL.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_suffixes:
            text = path.read_text(encoding="utf-8")
            if "\ufffd" in text:
                fail(f"UTF-8 replacement character found in {path.relative_to(ROOT)}")

    scripts = {path.name: path for path in (SKILL / "scripts").glob("*.py")}
    if set(scripts) != EXPECTED_SCRIPTS:
        fail(f"unexpected script set: {sorted(scripts)}")
    for path in scripts.values():
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        run(str(path), "--help")


def validate_specialist_skills() -> None:
    manifest = (SKILL / "manifest.yaml").read_text(encoding="utf-8")
    routing = (SKILL / "references" / "specialist-skill-routing.md").read_text(encoding="utf-8")
    bundled_root = SKILL / "bundled_skills"
    found = {path.name for path in bundled_root.iterdir() if path.is_dir()}
    if found != EXPECTED_SPECIALISTS:
        fail(f"unexpected bundled specialist set: {sorted(found)}")
    for name in sorted(EXPECTED_SPECIALISTS):
        entrypoint = bundled_root / name / "SKILL.md"
        if not entrypoint.is_file():
            fail(f"missing bundled specialist entrypoint: {name}/SKILL.md")
        text = entrypoint.read_text(encoding="utf-8")
        if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", text):
            fail(f"bundled specialist name mismatch: {name}")
        declared = f"{name}: bundled_skills/{name}/SKILL.md"
        if declared not in manifest:
            fail(f"manifest lacks specialist fallback: {name}")
        if f"`{name}`" not in routing:
            fail(f"routing reference lacks specialist: {name}")


def validate_external_catalogs() -> None:
    manifest = (SKILL / "manifest.yaml").read_text(encoding="utf-8")
    routing = (SKILL / "references" / "external-catalog-routing.md").read_text(encoding="utf-8")
    provenance = (SKILL / "bundled_catalogs" / "SOURCES.md").read_text(encoding="utf-8")
    root = SKILL / "bundled_catalogs"
    found = {path.name for path in root.iterdir() if path.is_dir()}
    if found != set(EXPECTED_CATALOGS):
        fail(f"unexpected bundled catalog set: {sorted(found)}")
    for name, expected_count in EXPECTED_CATALOGS.items():
        catalog = root / name
        skill_files = list(catalog.rglob("SKILL.md"))
        if len(skill_files) != expected_count:
            fail(f"catalog {name} expected {expected_count} skills, found {len(skill_files)}")
        license_file = catalog / "LICENSE"
        if not license_file.is_file() or "MIT License" not in license_file.read_text(encoding="utf-8"):
            fail(f"catalog {name} lacks preserved MIT license")
        if f"root: bundled_catalogs/{name}" not in manifest:
            fail(f"manifest lacks catalog root: {name}")
        if f"`bundled_catalogs/{name}/`" not in routing:
            fail(f"routing reference lacks catalog: {name}")
        if f"`{name}`" not in provenance:
            fail(f"provenance lacks catalog: {name}")


def validate_internal_inventory() -> None:
    audit = (SKILL / "references" / "lxq-functions-v2.5-zh.md").read_text(encoding="utf-8")
    required = [
        "对应 LXQ 版本：`2.7.0`", "调用强度", "light", "standard", "strict", "forensic",
        "score_delivery_quality.py", "score_grant_quality.py", "generate_eval_cases.py",
        "validate_eval_cases.py", "examples/01-08_*.md", "eval_cases/case_001-case_033_*",
        "validate_nsfc_template.py", "nsfc-2026-formal-application-template.docx",
    ]
    missing = [item for item in required if item not in audit]
    if missing:
        fail("Chinese internal inventory lacks v2.5 items: " + ", ".join(missing))


def validate_manuscript_engine() -> None:
    manifest = (SKILL / "manifest.yaml").read_text(encoding="utf-8")
    skill_router = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    engine = SKILL / "references" / "sci-manuscript-engine.md"
    contracts_dir = SKILL / "references" / "manuscript-contracts"
    full_contract = SKILL / "references" / "output_contracts" / "full_manuscript.md"
    regression = SKILL / "eval_cases" / "manuscript_engine_cases.md"

    required_files = [engine, full_contract, regression]
    missing_files = [str(path.relative_to(SKILL)) for path in required_files if not path.is_file()]
    if missing_files:
        fail("missing manuscript engine files: " + ", ".join(missing_files))

    found_contracts = {path.name for path in contracts_dir.glob("*.md")}
    if found_contracts != EXPECTED_MANUSCRIPT_CONTRACTS:
        fail(f"unexpected manuscript contract set: {sorted(found_contracts)}")

    required_manifest_tokens = [
        "manuscript_engine:",
        "references/sci-manuscript-engine.md",
        "references/manuscript-contracts/structure-narrative.md",
        "references/manuscript-contracts/evidence-story.md",
        "references/manuscript-contracts/reporting-statistics.md",
        "references/manuscript-contracts/visual-presentation.md",
        "references/output_contracts/full_manuscript.md",
    ]
    missing_tokens = [token for token in required_manifest_tokens if token not in manifest]
    if missing_tokens:
        fail("manifest lacks manuscript engine routing: " + ", ".join(missing_tokens))

    if "SCI Manuscript Engine" not in skill_router:
        fail("SKILL.md lacks SCI Manuscript Engine routing section")

    engine_text = engine.read_text(encoding="utf-8")
    for token in ("Evidence Map", "Scientific Story Engine", "Figure Storyboard", "Study-type router"):
        if token not in engine_text:
            fail(f"SCI manuscript engine lacks required concept: {token}")


def validate_profiles() -> None:
    scripts = SKILL / "scripts"
    scaffold = scripts / "scaffold_review.py"
    bundle_validator = scripts / "validate_review_bundle.py"
    issue_validator = scripts / "validate_issue_register.py"
    grant_validator = scripts / "validate_grant_delivery.py"
    literature_validator = scripts / "validate_literature_files.py"
    nsfc_validator = scripts / "validate_nsfc_template.py"
    nsfc_template = SKILL / "assets" / "templates" / "nsfc-2026-formal-application-template.docx"

    if not nsfc_template.is_file():
        fail("missing bundled NSFC formal application template")
    run(str(nsfc_validator), str(nsfc_template))

    with tempfile.TemporaryDirectory(prefix="lxq-repository-test-") as tmp:
        base = Path(tmp)
        for profile in ("core", "revision", "submission", "full", "grant", "literature", "complete"):
            bundle = base / profile
            run(str(scaffold), "--output", str(bundle), "--profile", profile)
            run(str(bundle_validator), str(bundle), "--profile", profile)
            run(str(issue_validator), str(bundle / "issue-register.tsv"), "--fail-on", "none")
            if profile in {"grant", "complete"}:
                run(str(grant_validator), str(bundle), "--language", "zh", "--allow-empty")
            if profile in {"literature", "complete"}:
                run(str(literature_validator), str(bundle / "literature-files.tsv"))


def validate_eval_and_scores() -> None:
    scripts = SKILL / "scripts"
    examples = list((SKILL / "examples").glob("*.md"))
    eval_files = list((SKILL / "eval_cases").glob("case_*"))
    contracts = list((SKILL / "references" / "output_contracts").glob("*.md"))
    if len(examples) != 12:
        fail(f"expected 12 examples, found {len(examples)}")
    if len(eval_files) != 99:
        fail(f"expected 99 eval files, found {len(eval_files)}")
    if len(contracts) != 9:
        fail(f"expected 9 output contracts, found {len(contracts)}")
    run(str(scripts / "validate_eval_cases.py"), str(SKILL / "eval_cases"))

    good_delivery = """# 拟定题目
# 研究背景与临床问题
# 研究假说
# 研究目标
# 主要研究内容
研究对象、方法、检测指标和预期判断明确。
# 拟解决的关键问题
# 研究对象与样本量
样本量120例，依据事件率和精度计算。纳入标准明确，排除标准明确。
# 分组、检测指标与随访节点
分组和对照明确；主要终点、次要终点和检测指标明确。
# 统计学与模型构建
采用回归模型，报告95%置信区间。
# 技术路线
# 创新点
# 可行性分析
预算3万元，使用常规指标。
# 风险与替代方案
风险明确，并提供替代方案。
# 预期成果
形成可复核结果。
"""
    bad_delivery = "预算3万元，多维度系统阐明机制，开展单细胞测序和空间组学，前期研究已证实有效。"
    good_grant = """# 研究背景与立项依据
目前临床患者管理困难在于风险识别不足，现有研究缺乏外部校准。
# 研究目标
评估指标并验证模型校准度。
# 研究内容
目标一对应队列构建；目标二对应验证。
# 创新点
在明确临床人群、时间点、评价指标、统计方法和数据验证路径中加入校准验证。
# 样本量
样本量120例，依据事件率、精度和失访计算。
# 统计方法
采用回归模型并报告置信区间。
# 经费
预算3万元，使用常规指标。
# 风险与替代方案
风险为随访缺失；替代方案为敏感性分析。
"""
    bad_grant = "# 立项依据\n具有重要理论意义和实践价值。\n# 目标\n系统阐明机制。\n预算2万元，开展单细胞测序。"

    with tempfile.TemporaryDirectory(prefix="lxq-score-test-") as tmp:
        tmp_path = Path(tmp)
        fixtures = {
            "good_delivery.md": good_delivery,
            "bad_delivery.md": bad_delivery,
            "good_grant.md": good_grant,
            "bad_grant.md": bad_grant,
        }
        for name, text in fixtures.items():
            (tmp_path / name).write_text(text, encoding="utf-8")

        def score(script: str, filename: str) -> dict[str, object]:
            completed = subprocess.run(
                [sys.executable, str(scripts / script), str(tmp_path / filename)],
                cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if completed.returncode != 0:
                fail(f"scorer failed: {script}\n{completed.stdout}")
            return json.loads(completed.stdout)

        gd = score("score_delivery_quality.py", "good_delivery.md")
        bd = score("score_delivery_quality.py", "bad_delivery.md")
        gg = score("score_grant_quality.py", "good_grant.md")
        bg = score("score_grant_quality.py", "bad_grant.md")
        if not (gd["score"] >= 85 and bd["score"] < 65 and gg["score"] >= 85 and bg["score"] < 65):
            fail(f"score separation failed: gd={gd['score']} bd={bd['score']} gg={gg['score']} bg={bg['score']}")


def main() -> int:
    required_root = {
        "README.md", "CONTRIBUTING.md", "SECURITY.md",
        "RELEASE_CHECKLIST.md", "CHANGELOG.md", "REGRESSION_REPORT.md",
        "VERSION", ".gitignore", ".gitattributes",
        ".github/workflows/validate.yml",
    }
    missing = [name for name in required_root if not (ROOT / name).is_file()]
    if missing:
        fail("missing repository files: " + ", ".join(sorted(missing)))
    validate_frontmatter()
    version = validate_manifest_paths()
    root_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != root_version:
        fail(f"version mismatch: manifest={version}, VERSION={root_version}")
    if version not in (ROOT / "README.md").read_text(encoding="utf-8"):
        fail("README does not mention the current version")
    if f"v{version}" not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        fail("CHANGELOG does not mention the current version")
    validate_text_and_scripts()
    validate_specialist_skills()
    validate_external_catalogs()
    validate_internal_inventory()
    validate_manuscript_engine()
    validate_profiles()
    validate_eval_and_scores()
    print(f"LXQ repository validation passed: version={version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
