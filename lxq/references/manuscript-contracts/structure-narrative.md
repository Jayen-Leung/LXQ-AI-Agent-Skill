# Manuscript Structure & Narrative Contract

## Scope

This contract adapts the useful structural ideas from the user-supplied `sci-paper-cn` material—funnel logic, section planning, paragraph jobs, forward references, and completeness checks—for biomedical and interdisciplinary scientific papers.

Do not copy the ResNet/CVPR hierarchy as a universal manuscript template.

## 1. Structure follows study type

Select section architecture only after study-type routing.

### Biomedical original article default

- Title
- Abstract
- Keywords when required
- Introduction
- Materials and Methods / Methods
- Results
- Discussion
- Conclusion when required or journal-specific
- Declarations
- References
- Supplementary materials

### Common overlays

Clinical observational:
- Study design and setting
- Participants
- Exposure/predictors
- Outcomes
- Covariates
- Statistical analysis

Prediction model:
- Data source/population
- Outcome definition
- Candidate predictors
- Missing data
- Model development
- Internal/external validation
- Calibration/discrimination/clinical utility

Bioinformatics + wet lab:
- Data acquisition
- Preprocessing/QC
- Discovery analysis
- Validation datasets
- Experimental validation
- Statistics

Single-cell/spatial:
- Data source/sample design
- QC/filtering
- normalization/integration/batch handling
- clustering/annotation
- differential/state/pathway analyses
- trajectory/communication/spatial analyses when used
- donor-level/statistical strategy

Do not include subsections solely because a template expects them.

## 2. Dynamic section budget

Plan length from target venue and evidence complexity.

Use proportional budgets when exact limits are unknown:

- Introduction: enough to establish the exact gap and objective, typically concise.
- Methods: enough for reproducibility; may be the longest section in complex omics or clinical-method papers.
- Results: proportional to the evidence chain and figure set.
- Discussion: proportionate interpretation, not a second Results section.

Never pad a manuscript to mimic a reference paper's page count.

## 3. Introduction narrative

Default funnel:

1. Disease/field significance or scientific problem.
2. Current biological/clinical understanding.
3. Specific unresolved gap, inconsistency, or limitation.
4. Why the unresolved issue matters scientifically or clinically.
5. Why existing approaches/evidence are insufficient.
6. Study rationale, hypothesis when appropriate, and objective.

Paragraph count is flexible.

Rules:

- Separate established knowledge from interpretation and hypothesis.
- Prefer primary and current sources for consequential claims.
- Do not claim "first", "novel", or "unprecedented" without explicit literature verification.
- End with an objective the design can actually answer.
- Avoid a generic roadmap paragraph unless the venue expects one.

## 4. Results narrative

Organize Results by scientific questions, not software modules or the chronological order of analysis.

Each subsection should have a job:

`Question -> approach -> observation -> quantitative/statistical support -> bounded meaning -> next question`

Good transitions create scientific necessity:

- "These findings prompted us to determine whether..."
- "To identify the cellular source of this association..."
- "We next tested whether this relationship was functionally causal..."

Do not use transitions to imply an experiment was performed when it was not.

## 5. Discussion narrative

The Discussion should answer:

1. What are the principal supported findings?
2. How do they compare with prior evidence?
3. What mechanisms or explanations are supported, plausible, or still speculative?
4. What alternative explanations, confounders, or biases remain?
5. What is the biological/clinical significance within the evidence boundary?
6. What are the most material strengths and limitations?
7. What conclusion is justified now?

Avoid:

- paragraph-by-paragraph repetition of Results;
- citation dumping;
- generic "future studies are warranted" without specifying the unresolved issue;
- converting association into mechanism or treatment recommendation.

## 6. Claim–Evidence–Interpretation–Boundary pattern

For consequential statements, use:

1. Claim: what was observed.
2. Evidence: figure/table/analysis/source.
3. Interpretation: what the observation likely means.
4. Boundary: what it does not establish.

Example pattern:

"Higher X expression was associated with worse overall survival in the discovery cohort (Fig. 2D; adjusted HR [value]). This supports X as a prognostic correlate in this dataset, but does not establish that X causally drives disease progression."

## 7. Forward-reference discipline

Reference figures/tables in the narrative before or at the point they are introduced.

Use the journal's preferred style:

- Figure/Fig.
- Table
- Supplementary Figure/Table
- Equation
- Section

Do not use vague references such as "the figure above" when a stable number exists.

## 8. Completeness check

For a complete manuscript verify:

- the section architecture matches the study design;
- every major section has a clear scientific job;
- the Introduction gap matches the study objective;
- Results answer the objective with traceable evidence;
- Methods reproduce the analyses/experiments actually used;
- Discussion claims remain inside the evidence boundary;
- Abstract and Title match the final paper, not an earlier draft;
- no required declaration or reporting item is silently omitted.
