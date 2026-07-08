# LXQ Regression Report

## Version

`2.5.0`

## Date

2026-07-08

## Evaluated cases

- 30 eval-case triplets: 10 grant direction screens, 5 customer deliveries, 5 bioinformatics plans, 5 wet-experiment plans, 3 literature readings, and 2 manuscript revisions.
- 7 structured review profiles.
- 4 positive/negative quality-scoring fixtures.
- Manifest routes, UTF-8 text, Python syntax, CLI entry points, and GitHub workflow structure.

## Passed cases

- 30/30 eval scaffolds passed structural and rubric validation.
- 7/7 review profiles generated and validated.
- Delivery and grant scorers separated positive fixtures (`>=85`) from negative fixtures (`<65`).
- Repository validation passed.

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
