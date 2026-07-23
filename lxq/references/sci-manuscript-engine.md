# LXQ SCI Manuscript Engine

## Purpose

This reference is the LXQ-native manuscript production layer for biomedical, clinical, bioinformatics, omics, wet-lab, translational, and mixed-method research papers.

It adapts useful contract-based patterns from the user-supplied `sci-paper-cn` specification—section planning, narrative contracts, figure/table completeness, cross-reference discipline, and submission-aware presentation—without importing its CVPR/ResNet-specific section hierarchy or fixed page budgets.

LXQ remains the authority for evidence boundaries, provenance, numerical consistency, research integrity, and readiness. Specialist writing, polishing, figure, citation, reading, and reviewer skills remain downstream executors.

## When to load

Load this reference when the user asks to:

- draft a complete scientific manuscript;
- convert data, results, figures, or a thesis/report into a paper;
- rebuild a manuscript's scientific story;
- write or substantially restructure Introduction, Methods, Results, Discussion, Abstract, or Title across the whole paper;
- create a paper from bioinformatics plus wet-lab evidence;
- prepare a journal-ready manuscript, preprint, or camera-ready scientific article;
- repair a manuscript whose figures, evidence, and narrative are misaligned.

For line editing or isolated paragraph polishing only, this engine is optional. Route directly to the relevant manuscript QC and specialist writing rules unless the problem is structural.

## Required companion references

When this engine is active, load:

1. `references/manuscript-qc.md`
2. `references/manuscript-contracts/structure-narrative.md`
3. `references/manuscript-contracts/evidence-story.md`
4. `references/manuscript-contracts/visual-presentation.md` when figures/tables/layout are in scope
5. `references/manuscript-contracts/reporting-statistics.md` for biomedical or quantitative work
6. exactly one primary output contract, normally `references/output_contracts/full_manuscript.md`

Also load only the actual component tracks involved: analysis, figure, literature, availability, revision, or integrated.

## Operating model

Use this order for complete manuscript work:

`fact base -> study-type routing -> evidence map -> scientific story -> figure storyboard -> Results -> Methods -> Discussion -> Introduction -> Abstract -> Title -> references/declarations -> cross-artifact QC -> specialist polish -> final validation`

This is the default production order, not necessarily the final document order.

### Why the production order differs from document order

Do not begin a full paper by freely drafting the Introduction. The scientific story must be constrained by the evidence that actually exists. Results and figures define the supported argument; Methods establish reproducibility; Discussion interprets within the evidence boundary; Introduction then frames the exact gap the completed study can address.

## Study-type router

Classify the manuscript before drafting. Select one primary study type and any secondary overlays.

Primary types:

- clinical observational or cohort;
- randomized/interventional clinical study;
- diagnostic/prognostic study;
- prediction/model development;
- bulk bioinformatics/transcriptomics;
- single-cell or single-nucleus omics;
- spatial omics;
- multi-omics/integrative analysis;
- wet-lab mechanism study;
- animal/preclinical study;
- translational hybrid;
- bioinformatics + wet-lab validation;
- systematic review/meta-analysis;
- methods/AI/ML paper.

Do not force a computer-science `Related Work -> Method -> Experiments` hierarchy onto biomedical manuscripts. Structure must follow study type, target journal, reporting guideline, and actual evidence.

## Dynamic section budget

Never hard-code an 8–12 page target or fixed paragraph count unless the target venue requires it.

Before drafting, define a section budget from:

- target journal or venue;
- article type;
- word/page limit;
- study design;
- number and complexity of figures/tables;
- supplementary-material policy.

If the venue is unknown, use a proportional budget rather than a fake exact word target. The manuscript must be complete but not padded.

## Scientific Story Engine

Before prose, write the paper's one-sentence argument:

`population/system -> unresolved question -> approach -> principal evidence -> bounded conclusion`

Then create a scientific-question chain in which each major result answers one question and creates the reason for the next analysis or experiment.

Example abstract pattern:

`clinical/biological problem -> unresolved gap -> study strategy -> principal quantitative/experimental findings -> bounded significance`

The story is not the chronological order in which analyses were performed. Reorder results when needed to create a defensible causal or evidentiary progression, but never hide contradictory, null, adverse, or sensitivity findings that materially qualify the conclusion.

## Figure-first rule

For data-rich papers, build a figure storyboard before writing Results.

Each main figure must have:

- one primary scientific question;
- one main claim;
- the evidence type and source;
- the strongest statistical/experimental support;
- the evidence strength;
- the transition question to the next figure.

A figure may contain multiple panels, but it should not be a miscellaneous container for unrelated analyses.

## Section generation order

### 1. Results

Write Results from the evidence map and figure storyboard, not from memory or generic prose.

Each subsection should follow:

`Question -> Method/analysis -> Observation -> Quantitative evidence -> Statistical evidence -> Interpretation boundary -> Transition`

Do not repeat Methods in detail. Do not expand association into mechanism.

### 2. Methods

Reconstruct Methods from actual data provenance, code, protocols, metadata, and author-provided facts.

Methods must support reproducibility and include all material choices that could alter interpretation: cohort construction, exclusions, preprocessing, QC, versions, parameters, covariates, statistical models, multiplicity, randomization/blinding when applicable, biological/technical replicates, ethics, software, databases, and figure/image processing.

### 3. Discussion

Discussion must integrate evidence, not restate Results.

Use the pattern:

`principal findings -> interpretation -> comparison with prior evidence -> mechanism/alternative explanations -> implications -> strengths -> limitations -> bounded conclusion/perspective`

The number of paragraphs is dynamic. Avoid generic template sentences when a concrete limitation or implication can be stated.

### 4. Introduction

Use a biomedical funnel:

`known problem -> current understanding -> unresolved gap/contradiction -> why the gap matters -> why existing approaches are insufficient -> study rationale/objective`

Do not claim novelty before verifying the literature. Do not write a gap that the study design cannot answer.

### 5. Abstract and Title

Write these only after the main argument is stable.

The abstract must reconcile population, sample size, design, primary methods, key quantitative findings, uncertainty, and conclusion with the main text.

The title must reflect design and evidence strength. Avoid causal language for purely observational work and avoid calling exploratory analysis a validated model.

## Specialist routing

After LXQ establishes the fact base and manuscript architecture:

- use `nature-writing` for section construction;
- use `nature-polishing` for language refinement after scientific structure is stable;
- use `nature-figure` for data-derived figures;
- use `nature-citation` and `nature-academic-search` for citation support and verification;
- use `nature-reader` for source-grounded full-paper reading;
- use `nature-reviewer` for an independent pre-submission review;
- use GPTomics/bioSkills leaf skills only to execute the actual omics analysis required to produce evidence.

External skills are evidence producers or writing executors. They may not override LXQ evidence boundaries.

## Mandatory non-fabrication labels

When a needed item is absent, preserve an explicit placeholder rather than inventing it.

Use as appropriate:

- `[USER_PROVIDED]`
- `[DATA_DERIVED]`
- `[LITERATURE_VERIFIED]`
- `[INFERRED]`
- `[AUTHOR_INPUT_NEEDED]`
- `[EVIDENCE_NEEDED]`
- `[POLICY_CHECK_NEEDED]`
- `[EXPERT_CONFIRMATION_NEEDED]`

Never fabricate sample size, P value, HR/OR/CI, AUC, effect size, accession number, PMID, DOI, software version, antibody catalog number, ethics approval, funding number, dataset identifier, or experimental result.

## Completion gate

A full manuscript is not complete merely because every heading has prose.

Before final delivery verify:

1. every central claim maps to evidence;
2. claim strength does not exceed evidence strength;
3. every main figure/table is referenced and explained;
4. all numerical values are consistent across abstract, text, figures, tables, supplements, and response materials;
5. study-specific reporting requirements are addressed;
6. citations supporting consequential claims are verified;
7. missing author facts remain visible;
8. figure legends and table notes are self-contained;
9. limitations are specific and proportionate;
10. final file format follows the actual journal/template, not a generic ResNet/CVPR style.
