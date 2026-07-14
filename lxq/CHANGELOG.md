# Changelog

## Unreleased

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
