# Output contract

Lead with the bounded outcome, not process narration.

Match output depth to invocation intensity. `light` returns a compact decision or shortlist; `standard` returns a complete task-specific deliverable; `strict` returns formal evidence-linked QC; `forensic` adds provenance, authenticity, and integrity-focused evidence handling. Do not force a light request into the full audit-report shape.

For a concise task, return:

1. `Outcome`: central finding or completed change.
2. `Scope`: artifacts actually reviewed and excluded.
3. `Critical issues`: blockers and major issues first.
4. `Actions`: completed repairs and remaining owner actions.
5. `Decision / readiness`: scientific decision plus package-readiness state when applicable.
6. `Verification`: reruns, recalculations, visual checks, schema checks, and unresolved gaps.

For a durable audit, use `references/output-schemas.md` and `references/report-template.md`.

## Placeholders and labels

- `[AUTHOR_INPUT_NEEDED: specific missing fact]`
- `[EVIDENCE_NEEDED: specific missing analysis or source]`
- `[POLICY_CHECK_NEEDED: current journal or regulatory rule]`
- `[EXPERT_CONFIRMATION_NEEDED: specialty and question]`

Do not hide these in prose. Keep them searchable and map them to issue IDs.

## Severity

- `Blocker`: invalidates identity, design, analysis, or central interpretation; stop downstream use.
- `Major`: could materially change a result, claim, or submission decision.
- `Minor`: improves reporting, reproducibility, or presentation without changing the central conclusion.
