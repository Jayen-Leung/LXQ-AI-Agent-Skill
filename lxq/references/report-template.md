# QC Report Template

## Scope

- Task modes and artifact tracks:
- Invocation intensity:
- Scientific question and intended use:
- Core claim, evidence, and boundary:
- Artifacts reviewed:
- Artifacts unavailable or not reviewed:
- Review date and environment:

## Decision

`PASS`, `CONDITIONAL PASS`, or `FAIL`

State exactly what the decision covers and what it does not certify.

## Package readiness

`ready_to_use`, `conditional`, `needs_author_input`, or `blocked`

Keep readiness separate from scientific decision.

## Executive findings

List the central conclusion, the strongest evidence, the most consequential limitation, and the minimum actions required before use or submission.

## Evidence and provenance

Describe source data, metadata, reference build/annotation, software/database versions, code or workflow entry point, and links between outputs and claims.

## Funding call alignment

For grant work, summarize the official call version and deadline, eligibility and scope constraints, mandatory sections, page or word limits, budget rules, and every unresolved compliance item. Link each requirement to the proposal location and its verification state.

## Specific aims and work plan

For grant work, map each aim to its question or hypothesis, rationale, preliminary evidence, design, experimental unit, primary outcome, analysis, success criterion, dependencies, risks, alternatives, deliverables, milestones, timing, owner, and budget line. Mark unsupported facts or commitments for author confirmation.

## Client-facing medical research delivery

For customer-facing work, summarize the client/department background, fund and budget, candidate-direction screen, selected title and hypothesis, directly readable scheme, and unresolved client facts. Confirm that innovation, feasibility, resource access, validation strength, budget fit, and client fit were considered for every proposed direction.

## Study-design completeness

For each grant aim or design component, report the research object, design and experimental unit, sample-size target and basis, groups/controls, inclusion/exclusion criteria, primary and secondary endpoints, time points, specimens/data, detection indicators, wet-lab plan, bioinformatics plan, validation, statistics, planned visuals, expected result, success criterion, and budget link.

## Literature corpus and acquisition provenance

For literature work, state the review question, databases and dates searched, exact query versions, screening and deduplication rules, included corpus, full-text status, lawful acquisition route, version, identifier, filename, size, SHA-256, and identity-verification status. Never imply that unavailable full text was reviewed.

## Evidence synthesis

For literature work, distinguish reported results from interpretation. Summarize study design, population or model, sample size, effect and uncertainty, support grade, bias or limitation, source anchor, consistency across studies, contradictions, and remaining evidence gaps.

## Issue register

| ID | Severity | Domain | Artifact/location | Finding | Evidence | Impact | Required action | Status | Verification |
|---|---|---|---|---|---|---|---|---|

Use stable IDs such as `DATA-001`, `STAT-001`, `TEXT-001`, and `FIG-001`.

Maintain the complete machine-readable register using [output-schemas.md](output-schemas.md), then validate it with `scripts/validate_issue_register.py`.

## Consistency matrix

| Claim/result | Source analysis | Table | Figure | Manuscript location | Status |
|---|---|---|---|---|---|

## Terminology and identifier consistency

Summarize locked terms, unresolved variants, group/endpoint labels, units, reference builds, and identifier namespaces.

## Changes performed

Record input, output, operation, rationale, tool/version, and whether scientific meaning changed.

## Verification performed

List reruns, recalculations, file inspections, visual checks, and unresolved validation gaps.

## Remaining limitations

Separate missing evidence, methodological limitations, generalizability, clinical limitations, and items requiring expert confirmation.

List every `[AUTHOR_INPUT_NEEDED]`, `[EVIDENCE_NEEDED]`, `[POLICY_CHECK_NEEDED]`, and `[EXPERT_CONFIRMATION_NEEDED]` item with its issue ID.

## Reproducibility handoff

List the manifest, code, environment, parameters, logs, result tables, edited documents, figures, and edit logs delivered.
