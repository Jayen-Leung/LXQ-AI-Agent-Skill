# Grant and Research Proposal QC

## Contents

1. Funding-call contract
2. Scientific case
3. Aims and work plan
4. Evaluation, feasibility, and risk
5. Budget and submission integrity
6. Customer-facing delivery

## Funding-call contract

Treat the current official funding call, sponsor instructions, application template, review criteria, page/word limits, eligibility rules, required attachments, and deadline/time zone as the governing specification. Record the exact scheme, year/cycle, applicant role, institution, project duration, requested amount, language, and intended review panel.

For a formal NSFC/国自然 Word application, read `references/nsfc-2026-formal-application-format-zh.md` and fill a copy of `assets/templates/nsfc-2026-formal-application-template.docx`. The bundled file is an institutional delivery template, not permanent proof of current NSFC policy. Preserve its required headings and form pages unless the verified current official system requires another structure.

Do not infer current eligibility, indirect-cost policy, page limits, submission fields, or deadlines from memory. Mark unresolved current requirements `[POLICY_CHECK_NEEDED: ...]` and verify official pages before final submission advice.

Build a compliance matrix:

| Requirement ID | Official requirement | Proposal location | Status | Owner | Verification |
|---|---|---|---|---|---|

## Scientific case

Write one bounded funding argument:

> The project addresses [important gap] in [population/system] by testing/developing [central idea], using [approach], supported by [preliminary evidence], to deliver [measurable outcome], within [scope and limitations].

Audit:

- importance and timeliness of the problem;
- precise knowledge or capability gap;
- innovation relative to the closest alternatives, without unsupported “first” claims;
- preliminary evidence and what it does not establish;
- fit to sponsor priorities and review criteria;
- expected scientific, clinical, societal, translational, or capacity-building value;
- ethical, inclusion, data-management, open-science, and stakeholder requirements when applicable.

Separate public evidence, applicant-generated preliminary results, institutional facts, planned work, and aspirations. Never invent pilot data, collaborators, facilities, letters, ethics approvals, costs, publications, or institutional commitments.

## Aims and work plan

Each aim should state: question/hypothesis, rationale, design, experimental unit, population/material, primary outcome, analysis, success criterion, dependency, risk, alternative, deliverable, milestone, owner, and timing.

Check that:

- aims are distinct but form one argument;
- later aims do not require an unvalidated result from an earlier aim without a contingency path;
- methods answer the stated aim and use the correct experimental unit;
- sample size, feasibility, recruitment/access, data generation, analysis, and timeline agree;
- work packages, milestones, deliverables, Gantt chart, personnel effort, and budget use the same scope and terminology;
- objectives are measurable without pretending uncertain research outcomes are guaranteed.

For medical research, explicitly record the study population, sample-size target and basis, groups and controls, inclusion/exclusion criteria, primary and secondary endpoints, time points, detection indicators, statistical method, expected result, and validation route. A target sample size without assumptions or rationale remains provisional.

## Evaluation, feasibility, and risk

Require explicit success criteria and decision rules. Distinguish scientific outcomes, process milestones, outputs, and longer-term impact. Check power or precision assumptions, access to participants/data/materials, recruitment or throughput, required expertise, infrastructure, governance, dependencies, and reproducibility.

For each material risk record probability, impact, early warning, mitigation, contingency, owner, and residual risk. A contingency must still answer a useful question; “repeat until successful” is not a plan.

## Budget and submission integrity

- Map every cost to an activity, work package, duration, and sponsor rule.
- Reconcile salary effort, equipment, consumables, travel, services, participant costs, data storage, publication/open-access costs, and indirect costs with the methods and timeline.
- Do not manufacture quotations, rates, institutional approvals, matching funds, or partner commitments.
- Treat missing letters, biosketches, facilities statements, data-management plans, ethics sections, budget justifications, and signatures as submission-readiness issues.

### Budget-to-method complexity guardrail

Use the following as an early design constraint, then verify local quotations and sponsor rules:

- `<= CNY 30,000`: prefer retrospective clinical data, small prospective observation, routine laboratory indicators, clinical scales, quantitative imaging, qPCR, IHC, ELISA, small tissue-microarray validation, or a simple machine-learning model. Do not default to single-cell/spatial omics, large proteomics/metabolomics, a multicentre prospective cohort, full animal mechanism validation, or large organoid screening.
- `CNY 30,000-50,000`: small mechanism validation, cell experiments, targeted assays, tissue microarrays, a basic risk model, or limited external validation may be feasible.
- `CNY 50,000-100,000`: multiple time points, an omics subcohort, exploratory animal/organoid work, more complete mechanism validation, or multimodal integration may be considered.
- `> CNY 100,000` or a major programme: multicentre cohorts, multi-omics, AI models, spatial/single-cell omics, systematic mechanism validation, and translational pathways may be designed only when platform, samples, personnel, duration, and governance support them.

For a low-budget, high-innovation request, prefer `clinical phenotype + routine indicators + small-scale validation + risk model`. Always reconcile the route with budget, duration, platform access, sample acquisition, and validation cost. These bands are heuristics, not quotations or guarantees.

Use `PASS`, `CONDITIONAL PASS`, or `FAIL` for reviewed scientific/compliance scope, and separately use `ready_to_use`, `conditional`, `needs_author_input`, or `blocked` for package readiness. Do not predict funding success.

Route prose construction to `nature-writing` after the fact base, compliance matrix, aims, evidence, and boundaries are established. Use fresh-reader testing on the near-final proposal to identify assumptions that make sense only to the applicant team.

For Chinese grant prose, apply `static/fragments/style/anti_ai_zh.md` before delivery without removing uncertainty, limitations, or author-input placeholders.

## Customer-facing delivery

When the requested output is a client-ready scheme, pre-sales document, or directly readable proposal, load `references/medical-research-delivery-zh.md` for Chinese output or `references/medical-research-delivery.md` for English output. Deliver the scheme in its customer-facing structure while retaining the funding-requirement, aim/work-plan, and study-design matrices as the auditable basis.

Do not let polished prose conceal missing sample-size justification, endpoints, inclusion/exclusion criteria, wet-lab controls, bioinformatics validation, budget mismatch, or unresolved client facts. Run `scripts/validate_grant_delivery.py` before assigning `ready_to_use`.

For formal NSFC DOCX output, additionally run `scripts/validate_nsfc_template.py <docx>` and complete a Word/PDF page render review. Structural validation does not replace scientific, policy, or applicant-fact review.
