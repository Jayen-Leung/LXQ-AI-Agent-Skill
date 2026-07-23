# Changelog

## Unreleased

## v2.9.0

### Added

- LXQ-native **SCI Manuscript Engine** for complete manuscript drafting, evidence-to-paper workflows, whole-paper reconstruction, and journal-ready scientific writing.
- Study-type routing for clinical observational/interventional research, diagnostic/prognostic studies, prediction models, bulk bioinformatics, single-cell/single-nucleus omics, spatial omics, multi-omics, wet-lab mechanism studies, animal studies, translational hybrids, bioinformatics + wet-lab papers, systematic reviews/meta-analyses, and AI/ML methods papers.
- Four manuscript contracts covering structure/narrative, evidence/scientific story, reporting/statistics, and visual presentation.
- Evidence-first manuscript workflow: `fact base -> study type -> evidence map -> scientific story -> figure storyboard -> Results -> Methods -> Discussion -> Introduction -> Abstract -> Title -> final QC`.
- Evidence Ladder (L0-L9) and claim-strength gate so causal/mechanistic language cannot exceed the available evidence.
- Figure Storyboard contract requiring each main figure to answer a defined scientific question, support one main claim, declare evidence strength, and create a transition to the next question.
- Biomedical reporting/statistics routing for CONSORT, STROBE, STARD, TRIPOD, PRISMA, ARRIVE, CARE, and SQUIRE-style requirements where applicable.
- Explicit safeguards against pseudoreplication, data leakage, overfitting, unverified multiplicity, unsupported clinical utility claims, and treating cell counts as biological replicate counts.
- Full-manuscript output contract with evidence map, scientific story, figure/table plan, manuscript, unresolved-evidence register, and QC/readiness output.
- Seven manuscript-engine regression scenarios covering bioinformatics + wet-lab papers, clinical cohorts, single-cell pseudoreplication, inappropriate CVPR-template forcing, causal overclaiming, missing experimental metadata, and figure-story reconstruction.

### Changed

- Complete manuscript tasks now route through the SCI Manuscript Engine before downstream writing/polishing specialists.
- `nature-writing`, `nature-polishing`, `nature-figure`, `nature-citation`, `nature-academic-search`, `nature-reader`, and `nature-reviewer` remain specialist executors; LXQ retains authority over evidence boundaries, numerical consistency, provenance, research integrity, and readiness.
- GPTomics/bioSkills remain evidence-producing analysis executors and may not be used as a substitute for evidence that was not actually generated.
- Manuscript structure is now selected dynamically by study type and target venue instead of inheriting a fixed CVPR/ResNet-style `Related Work -> Method -> Experiments` hierarchy.
- Section budgets are now journal/article-type dependent rather than fixed to an 8-12 page conference-paper target.
- The original `Claim -> Evidence -> Interpretation` pattern is extended to `Question -> Method -> Observation -> Quantitative/Statistical Evidence -> Interpretation Boundary -> Next Question` for biomedical Results writing.
- Introduction logic now uses a biomedical funnel: known problem -> current understanding -> unresolved gap/contradiction -> why it matters -> limitations of existing evidence -> study rationale/objective.
- Discussion is promoted to a first-class contract with principal findings, literature comparison, mechanistic/alternative interpretation, implications, strengths, limitations, and bounded perspective.
- Visual formatting now follows the actual journal/template first; the user-supplied `sci-paper-cn`/ResNet-CVPR typography is treated only as a design reference, not a universal submission format.

### Integrity and compatibility

- Preserved `light`, `standard`, `strict`, and `forensic` invocation intensities.
- Preserved `audit`, `repair`, `execute`, and `explain` task modes.
- Preserved LXQ non-fabrication boundaries and explicit placeholders such as `[AUTHOR_INPUT_NEEDED]`, `[EVIDENCE_NEEDED]`, and `[EXPERT_CONFIRMATION_NEEDED]`.
- The user-supplied `sci-paper-cn` structure/narrative/visual contracts were adapted conceptually into LXQ rather than copied as a computer-science conference template.

### Invocation examples

```text
LXQ strict：把这个项目做成一篇可投稿 SCI。
```

For a full evidence-to-paper workflow:

```text
调用 LXQ strict 模式处理本项目。先建立 Evidence Map、Evidence Strength Grading、Scientific Question Chain 和 Figure Storyboard，再按 Results -> Methods -> Discussion -> Introduction -> Abstract -> Title 的内部顺序构建全文，最后进行 citation/statistics/figure-text consistency/Nature reviewer/LXQ final QC。禁止虚构任何数据、统计量、文献、伦理号、基金号、软件版本、试剂货号或未完成实验。
```

## v2.8.0

### Added

- Canonical Chinese single-paper literature reading report structure based on the approved LXQ FOXN3/NEK6 report mode.
- Dedicated Word/PDF layout profile with title hierarchy, metadata table, evidence boxes, figure placement, evidence-strength matrix, article-use boundaries, and page-flow rules.
- On-demand routing for formal Chinese literature reading reports and established LXQ report formatting.

### Changed

- Literature reports now default to a structured evidence-led reading report rather than a loose abstract summary when the user requests a formal deliverable.
- Word remains the primary editable artifact; rendered page inspection is required before delivery.

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
