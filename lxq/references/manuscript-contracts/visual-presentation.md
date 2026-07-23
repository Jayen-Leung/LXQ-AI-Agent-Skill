# Manuscript Visual & Presentation Contract

## Purpose

Adapt the useful visual principles from the user-supplied `sci-paper-cn` style and figure/table guidance to biomedical and interdisciplinary manuscripts without treating ResNet/CVPR typography as a universal journal standard.

## 1. Journal/template authority

The target journal's official author instructions and template override this contract for:

- page size and margins;
- one- vs two-column layout;
- font family and size;
- abstract style;
- citation/reference format;
- figure/table placement;
- line numbering;
- title page and declaration requirements.

Never impose a CVPR double-column layout on a biomedical journal unless the target venue requires it.

## 2. General visual principles

- Every visual element must have a scientific purpose.
- Reference each figure/table at the point where its evidence enters the argument.
- Captions/legends must be sufficiently self-contained for scientific interpretation.
- Prefer vector output for plots and diagrams when the submission system permits it.
- Use raster formats at journal-appropriate resolution for microscopy, pathology, gels/blots, and other image data.
- Preserve readability at final publication size; do not rely on zoom.
- Maintain consistent terminology, units, group names, colors, symbols, and abbreviations across all figures and text.
- Accessibility and colorblind-safe differentiation are preferred; never encode a critical distinction by color alone when avoidable.

## 3. Figure-level scientific contract

Each main figure should define:

- primary scientific question;
- primary claim;
- panel-to-claim mapping;
- source data and analysis/assay;
- biological/statistical unit;
- key statistical test or validation;
- evidence boundary.

Avoid decorative panels that do not advance or validate the claim.

## 4. Biomedical figure types

Apply track-specific QC for common figures:

### Clinical/epidemiologic

- flow diagram / cohort attrition;
- baseline tables;
- Kaplan–Meier curves;
- forest plots;
- ROC/PR curves;
- calibration plots;
- decision-curve analysis;
- restricted cubic splines;
- subgroup/interaction plots.

### Omics/bioinformatics

- volcano/MA plots;
- heatmaps;
- enrichment plots;
- PCA/UMAP/t-SNE;
- dot/violin/feature plots;
- trajectories/pseudotime;
- cell–cell communication;
- spatial maps;
- multi-omics integration/network figures.

### Wet lab/mechanism

- microscopy/IHC/IF;
- western blots/gels;
- qPCR/bar or dot plots;
- flow cytometry;
- colony/transwell/wound healing;
- animal phenotype/survival;
- pathway/mechanism diagrams.

For detailed scientific-image integrity checks, also load `references/figure-qc.md`.

## 5. Figure legends

A legend should state as applicable:

- what was measured;
- experimental groups/conditions;
- what each panel shows;
- sample/replicate definition;
- summary statistic and error representation;
- statistical test and multiplicity handling;
- significance notation;
- scale bars, magnification, gating, normalization, or image processing details needed for interpretation;
- abbreviation definitions.

Do not move critical Methods into legends when the journal expects them in Methods, but legends must remain interpretable on their own.

## 6. Tables

Use journal-native table style. General rules:

- title/caption placement follows the journal template;
- avoid unnecessary vertical rules;
- align numeric precision meaningfully;
- state denominators, units, reference groups, effect measures, CI, and P/adjusted P values where relevant;
- distinguish descriptive from inferential statistics;
- define missing-data handling and footnotes;
- do not bold a "best" result unless that convention is scientifically meaningful for the table type.

The computer-science convention "best result in bold" is not a universal biomedical rule.

## 7. Equations and notation

Use equations only when they improve reproducibility or conceptual clarity.

- define all symbols;
- keep notation consistent with text and code;
- number equations only when they are referenced or the journal requires it;
- use the target template's math typography.

## 8. Typography and export

For drafts without a journal template:

- prioritize legible serif/sans-serif academic typography;
- use clear heading hierarchy;
- maintain high-contrast text;
- avoid ornamental visual styling;
- use consistent figure fonts and sizes.

For Chinese internal/advisor-review DOCX, use CJK-safe fonts appropriate to the requested deliverable. For final submission, the journal template controls typography.

## 9. Cross-artifact visual consistency gate

Before delivery verify:

- figure numbering and panel labels match text;
- legends match the actual plotted groups and statistics;
- axes, units, group colors, sample counts, and abbreviations are consistent;
- figure order matches the scientific-question chain;
- no figure is cited but missing;
- no supplied figure is silently excluded if it materially affects the conclusion;
- supplementary and main-figure references are correct.
