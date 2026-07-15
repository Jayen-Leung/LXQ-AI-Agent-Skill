# Changelog

## Unreleased

## v2.8.0

### Added

- 固化中文单篇文献阅读报告内容结构，包括核心结论、研究背景、研究思路、技术路线、分结果解读、机制证据链、创新性、LXQ证据强度、局限、后续方向和文章适用边界。
- 新增 `references/literature-report-word-style-zh.md`，统一 Word/PDF 的标题、表格、色系、图表排布、页眉页脚和分页规则。

### Changed

- 正式文献阅读报告不再输出松散摘要，默认按证据链组织，并将原文结果图放在对应结果段落附近。
- 用户要求 Word、PDF 或既定 LXQ 格式时，必须加载版式规范并完成渲染检查。

## v2.5.1

### Added

- Three red-team regression cases for low-budget high-cost omics, unverified applicant facts, and fake DOI/literature evidence.
- Hard-flag outputs in grant and customer-delivery scoring scripts.

### Changed

- Eval scaffold now contains 33 cases instead of 30.
- Delivery and grant quality scorers now require bounded sample-size evidence rather than accepting the word "样本量" alone.
- Budget mismatch detection now covers single-cell, spatial omics, WES/WGS, full exome/genome, and other high-cost methods.
- Scoring payloads now include `readiness` for internal review.

### Added

- Reusable 2026 NSFC formal-application DOCX template asset.
- Five-page Chinese NSFC delivery format and exact page-layout contract.
- Dependency-free `validate_nsfc_template.py` structural validator.

## v2.5.0

### Added

- Invocation intensity levels: light, standard, strict, forensic.
- Chinese anti-AI style filter.
- Budget-to-method matching rules.
- Topic scoring rubric for customer-facing medical research directions.
- Examples and bad examples structure.
- Eval cases scaffold.
- Delivery and grant quality scoring scripts.
- Regression report template.
- Task-specific output contracts.

### Changed

- Routing now identifies invocation intensity before task mode and functional tracks.
- Chinese customer delivery rules now enforce a stricter 14-section default structure.
- Low-budget grant design now limits high-cost omics and animal experiments unless explicitly requested.

### Preserved

- Existing audit/repair/execute/explain modes.
- Existing evidence discipline and research integrity boundaries.
- Existing validation scripts and structured review bundle logic.
