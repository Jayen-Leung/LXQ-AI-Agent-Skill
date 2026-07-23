# Biomedical Reporting & Statistics Contract

## 1. Reporting-guideline router

Select the applicable reporting standard when the study type is known. Examples include:

- randomized trials: CONSORT;
- observational studies: STROBE;
- diagnostic accuracy: STARD;
- prediction models: TRIPOD or current successor/update required by the target venue;
- systematic reviews/meta-analyses: PRISMA;
- animal studies: ARRIVE;
- case reports: CARE;
- quality-improvement studies: SQUIRE when applicable.

Use current official guidance when formal compliance is required. Do not claim compliance unless the required items were actually checked.

For omics, single-cell, spatial, AI/ML, and emerging study types, apply journal/community reporting expectations plus reproducibility rules rather than inventing a universal checklist.

## 2. Statistical unit and replication

Identify before inference:

- experimental unit;
- biological replicate;
- technical replicate;
- participant/donor/sample hierarchy;
- repeated measures or clustered observations.

Critical rule for single-cell and similar high-dimensional data:

`cells are not automatically independent biological replicates`.

Do not inflate n by treating cells, fields, images, technical wells, or repeated measurements as independent subjects unless the model explicitly accounts for clustering and the scientific estimand supports it.

## 3. Minimum statistical reporting

As applicable report:

- sample size and denominator;
- descriptive statistic appropriate to distribution;
- effect size;
- uncertainty (typically CI);
- exact or appropriately formatted P values;
- multiplicity/adjustment status;
- missing-data handling;
- model covariates and assumptions;
- validation strategy;
- software/package/version when material to reproducibility.

Statistical significance is not equivalent to biological or clinical importance.

## 4. Model and analysis risk checks

Check when applicable:

- paired vs unpaired design;
- repeated measures/clustering;
- parametric assumptions;
- sparse or imbalanced outcomes;
- confounding and covariate selection;
- multiple comparisons;
- data leakage;
- overfitting;
- optimism correction;
- internal vs external validation;
- calibration as well as discrimination;
- proportional-hazards assumptions;
- nonlinear relationships;
- competing risks;
- batch effects;
- pseudoreplication;
- post hoc subgroup analyses;
- sensitivity analyses.

## 5. Prediction/ML manuscripts

Do not present a model as clinically useful based only on training-set or internal AUC.

Separate:

- development;
- tuning;
- internal validation;
- external validation;
- calibration;
- clinical utility;
- interpretability.

Explicitly audit leakage between preprocessing/feature selection and cross-validation folds.

## 6. Omics manuscripts

Report and audit as applicable:

- data source/accession;
- reference build/database versions;
- preprocessing/QC thresholds;
- normalization;
- batch handling;
- contrasts;
- multiple-testing correction;
- covariates;
- donor/sample-level inference;
- independent validation;
- pathway/database version;
- random seeds or stochastic settings when relevant.

## 7. Reproducibility gate

A Methods section is not ready if material parameters are replaced by vague phrases such as "standard methods were used" when those choices could alter results.

Mark unresolved items as:

- PASS
- WARNING
- MISSING
- CRITICAL

Never fill a missing parameter, version, ethics number, accession, antibody identifier, or sample count from guesswork.
