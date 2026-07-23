# Manuscript Evidence & Scientific Story Contract

## 1. Evidence-first principle

A manuscript is a structured argument built from evidence, not a sequence of analyses and not a prose expansion of figure legends.

Before drafting, create an evidence map for every central claim.

Minimum fields:

| Claim ID | Scientific question | Exact claim | Evidence artifact | Data/source | Method | Quantitative/statistical support | Evidence level | Allowed wording | Boundary |
|---|---|---|---|---|---|---|---|---|---|

Every Abstract conclusion and every major Discussion claim must trace to at least one row.

## 2. Evidence ladder

Use the ladder as a claim-strength guardrail, not as a universal hierarchy of study quality.

- L0: hypothesis or rationale only.
- L1: single-dataset association or exploratory observation.
- L2: independent cohort/dataset replication.
- L3: cross-modal, multi-omics, single-cell, or spatial convergence that improves localization/consistency but may remain associative.
- L4: clinical tissue/specimen or orthogonal assay validation.
- L5: controlled in-vitro perturbation demonstrating functional effect.
- L6: mechanism-specific perturbation with pathway or mediator evidence.
- L7: rescue/epistasis or direct biochemical evidence supporting a causal mechanism.
- L8: in-vivo validation with an appropriate disease model.
- L9: prospective/interventional or high-grade human validation where applicable.

Do not mechanically assume L9 is required for all basic-science claims, or that a higher number automatically means better evidence for a different question.

## 3. Claim strength must not exceed evidence strength

Examples:

Association only:
- Prefer: "X was associated with Y" or "X correlated with Y".
- Avoid: "X drives Y".

Functional perturbation:
- May support: "X promoted/inhibited phenotype Y in the tested model".
- Does not by itself prove the complete molecular mechanism.

Mechanistic rescue or direct biochemical evidence:
- May support a pathway-specific causal claim within the tested system.
- Do not automatically generalize to patients or therapeutic efficacy.

Animal evidence:
- Supports in-vivo biological relevance in the model.
- Does not establish clinical benefit.

## 4. Scientific-question chain

Build the paper as a chain of questions.

Example for a translational mechanism paper:

1. Is X altered in disease?
2. Is the alteration clinically or biologically relevant?
3. In which cells/tissues/states is X localized?
4. Which pathways/processes are associated with X?
5. Does perturbing X change the phenotype?
6. Through which mediator/pathway does the effect occur?
7. Can rescue/epistasis/direct evidence establish the proposed mechanism?
8. Does the mechanism hold in vivo or in human tissue?

Skip questions that are irrelevant. Do not add analyses simply to make the chain longer.

## 5. Figure storyboard

Before writing a data-rich Results section, create a storyboard.

Minimum fields:

| Figure | Scientific question | Main claim | Panels/evidence | Evidence level | Critical statistic/validation | Transition to next figure |
|---|---|---|---|---|---|---|

Rules:

- one main figure = one primary scientific question whenever possible;
- a panel must contribute to the figure-level claim;
- redundant analyses belong in supplement unless they materially strengthen the claim;
- figure order should maximize scientific logic, not mirror the analyst's execution history;
- null or contradictory findings that qualify a conclusion must remain visible.

## 6. Results writing pattern

For each major result:

1. Scientific question.
2. Analysis/experiment used to answer it.
3. Observation.
4. Quantitative evidence.
5. Statistical or experimental support.
6. Bounded interpretation.
7. Transition to the next question.

Keep exact numeric reporting consistent with the source output.

## 7. Evidence producers vs manuscript writers

Bioinformatics, statistical, imaging, and experimental specialist skills produce evidence.

Writing/polishing skills produce prose.

Neither may silently invent missing evidence.

LXQ owns the linkage:

`source data/protocol -> analysis/experiment -> output -> figure/table -> claim -> manuscript sentence -> conclusion`

## 8. Contradictory and negative evidence

Do not remove evidence merely because it weakens the preferred story.

For material contradictions:

- identify whether they reflect technical variation, cohort heterogeneity, model dependence, multiplicity, low power, confounding, or a genuinely competing biological explanation;
- state the discrepancy in the evidence map;
- qualify the claim and Discussion accordingly.

## 9. Required labels for unresolved facts

Use explicit labels rather than fabrication:

- `[USER_PROVIDED]`
- `[DATA_DERIVED]`
- `[LITERATURE_VERIFIED]`
- `[INFERRED]`
- `[AUTHOR_INPUT_NEEDED]`
- `[EVIDENCE_NEEDED]`
- `[EXPERT_CONFIRMATION_NEEDED]`

These labels are working-state metadata and may be removed from the final manuscript only after the underlying fact is resolved.
