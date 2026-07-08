# Core workflow

Run these steps for every LXQ task.

## 1. Fix scope and authorization

Identify task intent, invocation intensity, task mode, artifact tracks, intended use, artifacts available, artifacts missing, and what may be changed. Preserve the review boundary explicitly.

## 2. Build the research fact base

Write one bounded statement:

> In [population/system], the project claims [finding/advance] using [design/approach], supported by [evidence], with [boundary and unresolved uncertainty].

If the statement cannot be written from supplied evidence, record `[EVIDENCE_NEEDED: ...]` rather than inventing a premise.

## 3. Build the terminology ledger

Lock canonical sample groups, cohort names, endpoints, assays, gene/protein/variant identifiers, units, abbreviations, software names, reference builds, figure labels, and manuscript terms. Reuse them across data, code, tables, figures, prose, supplements, and response letters.

## 4. Pass the identity gate

Verify IDs, pairing, groups, units, assay, build/reference, annotation, and file provenance before statistics or interpretation. Identity failures are blockers.

## 5. Use an alignment gate only for high-leverage ambiguity

Before a large repair, rerun, or manuscript-wide change, show the fact-base sentence, selected modes/tracks, primary assumptions, and at most three high-leverage questions when a wrong answer would materially redirect the work. Skip the gate when scope and evidence are already clear. If the user elects to proceed without missing information, create a bounded scaffold with placeholders.

## 6. Apply stage-aware quality gates

Check in order: identity, design, input state, data quality, computation, statistics, consistency, interpretation, and integrity. Do not let a downstream pass compensate for an upstream failure. Load the selected artifact references for detailed checks.

For each consequential cutoff, record whether it is `hard-validity`, `protocol`, `cohort-relative`, `heuristic`, or `exploratory`. Missing metrics are not passes.

## 7. Perform the authorized mode

- Audit: diagnose and grade; do not silently mutate artifacts.
- Repair: change only evidence-supported defects and log meaning changes.
- Execute: record versions, parameters, seeds, references, order, logs, and rerun status.
- Explain: distinguish what is shown, inferred, uncertain, and not assessable.

## 8. Link claims to evidence and availability

Map each central claim to source data, analysis, result table, display artifact, manuscript location, citation status, limitation, and availability location. A figure is not automatically the numerical source. A title-level citation match is not verified support.

## 9. Revise locally and recheck propagation

Prefer targeted edits over full rewrites. If a correction forces structural change, state it. Recheck every downstream consumer of a changed value, label, term, threshold, panel, or claim. Preserve stable issue, claim, reviewer-comment, and change IDs.

## 10. Assign decision and package readiness

Keep scientific decision separate from handoff readiness:

- Decision: `PASS`, `CONDITIONAL PASS`, or `FAIL` within reviewed scope.
- Readiness: `ready_to_use`, `conditional`, `needs_author_input`, or `blocked`.

Use `[AUTHOR_INPUT_NEEDED: ...]` for facts only the author/project owner can supply. An unresolved blocker normally requires `FAIL` and `blocked`; unresolved major issues preclude `PASS`.

## 11. Run final QA

Check completeness, traceability, factuality, terminology, numerical consistency, tone, privacy, file integrity, visual exports, expected sample roster, repository identifiers, and unresolved risks. Open generated artifacts and rerun modified code where feasible.
