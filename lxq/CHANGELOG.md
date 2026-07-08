# Changelog

## Unreleased

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
