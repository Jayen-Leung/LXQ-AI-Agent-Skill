# Manuscript QC Reference

## Contents

1. Evidence map
2. Section review
3. Numerical consistency
4. Revision workflow
5. Reporting integrity

## Evidence map

For each central claim, record:

| Claim ID | Exact claim | Evidence artifact | Analysis/source | Support level | Required change |
|---|---|---|---|---|---|
| C1 | Manuscript sentence or distilled claim | Figure/table/result | Script, dataset, citation | Supported/partial/unsupported | Keep/qualify/correct/remove |

Trace every abstract conclusion and major discussion claim. Mark evidence that is indirect, exploratory, underpowered, uncorrected, internally derived, or dependent on an unverified citation.

Before line editing, write the manuscript's one-sentence argument as `population/system -> claim -> approach -> evidence -> boundary`. Build a terminology ledger for recurring cohort names, endpoints, assays, methods, identifiers, units, abbreviations, and notation. Treat inconsistent terminology as a cross-artifact defect, not stylistic variation.

## Section review

### Title and abstract

- Match design and evidence: do not label observational work as causal, exploratory work as validation, or a model as clinically useful without appropriate validation.
- Reconcile population, sample size, endpoint, effect direction, uncertainty, and conclusion with the main text.
- Avoid claims not shown in results.

### Introduction

- Distinguish established knowledge, controversy, gap, and study objective.
- Verify current, primary, and appropriate citations for consequential claims.
- End with a question or objective that the design can answer.

### Methods

- Make cohort construction, exclusions, assay, preprocessing, QC, reference/database versions, statistical model, covariates, contrasts, multiplicity, software, and ethics reproducible.
- Explain deviations from preregistration or protocol.
- Describe image processing and figure assembly that could affect interpretation.

### Results

- Present denominators and attrition before inferential results.
- Report effect size, uncertainty, exact or appropriately formatted P values, and multiplicity status.
- Keep observation separate from interpretation.
- Reconcile text with figures, tables, supplements, and output files.

### Discussion

- Start from supported findings, not aspirations.
- Compare with prior evidence without cherry-picking.
- State alternative explanations, biases, generalizability, unresolved confounding, and validation needs.
- Avoid turning association into mechanism or clinical recommendation.

### Data, code, and ethics statements

- Ensure accession numbers, repositories, restrictions, licenses, consent/ethics approvals, and code availability are accurate and mutually consistent.
- Do not expose protected or re-identifiable information.

## Numerical consistency

Cross-check:

- Sample and participant counts at every stage.
- Percentages against numerators and denominators.
- Units, decimal places, confidence intervals, P values, adjusted P values, and effect directions.
- Gene/protein/variant names, italics, transcript/build, cohort labels, time points, and treatment groups.
- Figure panel citations, table numbers, supplement references, and legend definitions.
- Abstract, main text, tables, figures, supplement, response letter, and repository outputs.

Treat discrepancies in central endpoints or sample counts as Major or Blocker, not copyediting.

## Revision workflow

1. Freeze the source version and create a revision copy.
2. Resolve scientific and numerical issues before stylistic polishing.
3. Keep a change log with location, old meaning, new meaning, evidence, and whether author confirmation is required.
4. For reviewer responses, quote or summarize each comment faithfully, state the action, identify manuscript locations, and avoid claiming an experiment or analysis was performed unless verified.
5. Re-run the consistency audit after all edits; late edits commonly create new mismatches.
6. Prefer targeted revision over full rewriting. When a correction forces structural change, identify the affected argument or paragraph map and recheck only the downstream sections and artifacts that consume it.

For manuscript-wide drafting or repair, separate section architecture, paragraph job, claim/evidence/boundary, and sentence polish. Do not improve sentence style while leaving a wrong section job or unsupported central argument intact.

## Reporting integrity

- Never invent references, values, analyses, ethics approvals, accession numbers, or reviewer-requested experiments.
- Never hide null, adverse, contradictory, or sensitivity results that materially qualify the conclusion.
- Label hypotheses generated after seeing results.
- Distinguish language editing from substantive scientific revision.
- Flag text that may require author, statistician, pathologist, geneticist, or clinician confirmation.
