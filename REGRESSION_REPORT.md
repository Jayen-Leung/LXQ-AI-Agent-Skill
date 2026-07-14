# LXQ Regression Report

## Version

`2.7.0`

## Date

2026-07-08

## Evaluated cases

- 33 eval-case triplets: 11 grant direction screens, 6 customer deliveries, 5 bioinformatics plans, 5 wet-experiment plans, 4 literature readings, and 2 manuscript revisions.
- 7 structured review profiles.
- 4 positive/negative quality-scoring fixtures.
- Manifest routes, UTF-8 text, Python syntax, CLI entry points, and GitHub workflow structure.
- Nine bundled Nature specialist skills and all declared specialist-routing fallback paths.
- GPTomics and Orchestra catalog snapshots, licenses, provenance, skill counts, and routing declarations.

## Passed cases

- 33/33 eval scaffolds passed structural and rubric validation.
- 7/7 review profiles generated and validated.
- Delivery and grant scorers separated positive fixtures (`>=85`) from negative fixtures (`<65`).
- Repository validation passed.
- 9/9 specialist skill entrypoints and routing declarations passed structural validation.
- GPTomics 562/562 and Orchestra 98/98 catalog entrypoints passed inventory validation.

## Failed cases

None in structural and deterministic regression tests.

## Average score

Not calculated. The current eval set defines inputs, expected behavior, and rubrics; it does not contain model response outputs. Reporting an average model score without running the held-out responses would be misleading.

## Major regressions

None detected in the existing review-bundle, literature-file, grant-delivery, issue-register, or provenance-manifest workflows.

## Improved behaviors

- Lightweight direction requests no longer default to full QC output.
- Complete Chinese delivery uses a 14-section contract.
- Low-budget proposals trigger high-cost-method warnings.
- Chinese template phrases are flagged for revision.
- Direction screening uses an eight-dimension internal score.

## New risks

- Quality scorers use transparent heuristics and may produce false positives or false negatives.
- Example quality and rubric weights still require periodic domain-expert review.
- Model-level average scores require a separate held-out response run.

## Required fixes before release

- Select a repository license.
- Run model responses against the 30 held-out cases before making benchmark claims.
- Obtain at least one independent medical-research and one statistical review of examples and rubric weights.
