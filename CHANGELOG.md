# Changelog

## Unreleased

## v2.7.0

### Added

- Complete MIT-licensed source snapshots of GPTomics bioSkills (562 skills) and Orchestra Research AI-Research-SKILLs (98 skills).
- Catalog-level automatic routing for bioinformatics/omics and AI/ML research tasks.
- Source provenance with pinned upstream commit hashes and preserved upstream licenses.
- Validation for catalog counts, licenses, provenance, and routing declarations.

### Changed

- External catalog instructions are explicitly subordinate to LXQ authorization, evidence, safety, privacy, and readiness gates.

## v2.6.0

### Added

- Bundled complete source copies of nine Nature specialist skills: writing, polishing, figure, response, citation, academic search, reader, data, and reviewer.
- Declarative specialist routing with installed-skill preference and bundled fallback behavior.
- Repository validation for the specialist inventory, entrypoints, routing coverage, and fallback paths.

### Changed

- LXQ now selects the smallest appropriate specialist set after establishing its evidence fact base and preserves LXQ ownership of cross-artifact QC and readiness.

## v2.5.1

### Added

- Three red-team regression cases for low-budget high-cost omics, unverified applicant facts, and fake DOI/literature evidence.
- Hard-flag outputs in grant and customer-delivery scoring scripts.

### Changed

- Eval scaffold now contains 33 cases instead of 30.
- Delivery and grant quality scorers now require bounded sample-size evidence rather than accepting the word "样本量" alone.
- Budget mismatch detection now covers single-cell, spatial omics, WES/WGS, full exome/genome, and other high-cost methods.
- Scoring payloads now include `readiness` for internal review.

- Added a reusable 2026 NSFC formal-application DOCX template asset.
- Added the Chinese NSFC five-page delivery contract, exact layout rules, and formal-grant routing.
- Added `validate_nsfc_template.py` for dependency-free DOCX structure and page-layout validation.

## v2.5.0

### Added

- Invocation intensity levels: light, standard, strict, forensic.
- Chinese anti-AI style filter.
- Budget-to-method matching rules.
- Topic scoring rubric for customer-facing medical research directions.
- Twelve positive/bad examples and a 30-case eval scaffold.
- Delivery and grant quality scoring scripts.
- Regression report template and eight task-specific output contracts.

### Changed

- Routing identifies invocation intensity before task mode and functional tracks.
- Chinese customer delivery uses a stricter 14-section structure.
- Low-budget design avoids high-cost omics and animal experiments unless explicitly requested.

### Preserved

- Audit/repair/execute/explain modes.
- Evidence discipline, privacy, image integrity, and non-fabrication boundaries.
- Existing structured review bundles and validators.
