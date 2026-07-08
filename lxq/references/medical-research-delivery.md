# Medical Research Delivery

## Purpose and boundary

Produce client-ready medical research content for topic selection, funding applications, and pre-sales delivery. Cover the research background, aims, work packages, key questions, innovation, technical route, wet-lab plan, bioinformatics plan, study design, statistics, expected outputs, and references.

Minimum delivery fields: client background, funding scheme and budget, sample size and rationale, inclusion/exclusion criteria, primary and secondary endpoints, measurements, wet-lab plan, bioinformatics plan, statistics, validation, and expected outputs.

Use this track when the user supplies or requests any of the following:

- hospital, department, investigator, or client background;
- funding scheme, budget, application guide, or review criteria;
- disease area, clinical problem, assay, omics, AI, or other technical direction;
- a directly readable customer-facing or application-ready scheme;
- formal, specific, non-generic language with minimal AI-like filler.

Do not use the output as unverified clinical advice, ethics approval, regulatory clearance, or the final sign-off of a statistician or domain expert. Never fabricate citations, guidelines, preliminary results, recruitment capacity, ethics status, facilities, collaborators, quotations, or a proven mechanism.

## Delivery workflow

### 1. Build the client and funding brief

Record the client type and department, clinical or scientific strengths, available cohorts/samples/data/platforms, prior work, intended fund, current call, duration, budget ceiling, application deadline, preferred technology, and constraints. Label missing facts `[AUTHOR_INPUT_NEEDED: ...]`; label current rules `[POLICY_CHECK_NEEDED: ...]` until checked against the official source.

### 2. Screen research directions

When the direction is not fixed, provide a short list before drafting the full scheme. For each direction state:

- proposed title and one-sentence central hypothesis;
- fit to the client background and fund scope;
- clinical or scientific gap and closest competing approach;
- innovation that can be defended without an unsupported "first" claim;
- feasibility of recruitment, sample access, platform, personnel, duration, and validation;
- budget fit and the main cost drivers;
- expected deliverable, principal risk, and fallback;
- recommendation: `prioritize`, `reserve`, or `do_not_recommend`.

If a numeric screen is useful, score client fit, scientific value, innovation, feasibility, resource access, budget fit, and validation strength. State the weights as project-specific heuristics rather than universal truth.

### 3. Establish the evidence boundary

Separate verified public evidence, client-supplied facts, directly verified client evidence, planned work, assumptions, and unresolved items. Use `nature-academic-search` or `nature-citation` for literature support. Do not turn a plausible rationale into an established mechanism.

### 4. Design the study before polishing prose

For every selected direction specify:

- research object, setting, design, experimental unit, sample-size target and basis;
- groups, controls, randomization/blinding where applicable, inclusion and exclusion criteria;
- primary endpoint, secondary endpoints, time points, biospecimens/data, and detection indicators;
- statistical analysis, missing-data handling, multiplicity, sensitivity analyses, and success criteria;
- expected result phrased as a testable expectation, not a guaranteed outcome.

If sample size cannot yet be calculated, give the calculation framework and assumptions needed, then mark the number as `proposed` or `[AUTHOR_INPUT_NEEDED]`. A convenient number without a basis is not an acceptable final sample size.

### 5. Specify wet-lab and bioinformatics plans

For wet-lab work include sample handling, assay/platform, experimental and negative/positive controls, biological and technical replicates, batch strategy, QC thresholds, primary readouts, orthogonal validation, failure criteria, and fallback methods.

For bioinformatics work include data source and access status, preprocessing, reference/build and annotation, feature definition, core algorithms, parameter and version recording, training/validation/test separation, leakage control, internal and external validation, wet-lab or clinical validation where relevant, performance metrics, interpretability, sensitivity analysis, and planned visualizations.

Do not list fashionable methods without explaining which aim they answer, what input they require, and how the result will be validated.

## Default customer-facing structure

Use the following order unless the funding template governs a different order:

1. Proposed title
2. Research background and rationale
3. Research objectives
4. Main research content
5. Key questions to resolve
6. Technical route and methodological design
7. Sample size and study population
8. Statistics and model development
9. Innovation
10. Feasibility
11. Expected outputs
12. References

Within the technical-route section, show the sequence from population/sample or data acquisition through experiment/computation, validation, interpretation, and deliverables. Keep a one-to-one mapping among aims, work packages, methods, endpoints, analyses, figures, milestones, and budget lines.

## Writing contract

- Lead with a usable deliverable, not generic advice.
- Use formal, concrete language; remove slogans, repetitive transitions, and template filler.
- Tie every direction to innovation, feasibility, budget, and client background.
- Use `recommended`, `proposed`, `planned`, or `requires confirmation` for uncertainty; do not write assumptions as settled facts.
- Distinguish association, prediction, causality, and mechanism.
- Cite only verified sources and keep claim-to-citation correspondence auditable.
- Present expected results as measurable outcomes and decision criteria, not promises.

## Completion gate

Before delivery confirm all applicable items:

- a sample-size target and defensible basis are present;
- inclusion and exclusion criteria are present;
- primary and secondary endpoints are explicit;
- grouping, controls, detection indicators, and time points are explicit;
- statistical methods match the design, endpoint, and experimental unit;
- the bioinformatics plan names data, algorithms, validation, metrics, and visual outputs;
- the wet-lab plan names assays, controls, replicates, QC, and orthogonal validation;
- causal or mechanistic language does not exceed the design;
- costs, sample throughput, platforms, personnel, and duration fit the budget;
- unsupported facts and unresolved requirements are visibly labelled;
- the final scheme is directly readable by the client and free of obvious AI filler.

If a required item is unavailable, return `needs_author_input` or `conditional`; do not call the scheme complete.

Validate an English customer scheme with `scripts/validate_grant_delivery.py <bundle> --language en`.
