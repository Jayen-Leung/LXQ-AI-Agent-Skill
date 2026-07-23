# Full Manuscript Output Contract

Use `standard` for complete drafting from adequate supplied evidence and `strict` for submission-ready, repair, or pre-submission work.

## Required workflow output before or alongside the manuscript

1. Study-type classification and target-venue assumptions.
2. One-sentence manuscript argument.
3. Evidence map for central claims.
4. Figure/storyboard map when figures or data-rich results are involved.
5. Explicit unresolved facts/placeholders.

For a user who only wants the clean final manuscript, keep these working artifacts internal unless a scientific blocker requires author input; still perform the checks.

## Final manuscript completeness

Return all sections required by the actual study type and target journal. Do not invent a universal section hierarchy.

Typical biomedical original article:

- Title
- Authors/affiliations only when supplied
- Abstract
- Keywords when required
- Introduction
- Materials and Methods / Methods
- Results
- Discussion
- Conclusion when appropriate
- Declarations required by the venue
- References
- Supplementary-material references when applicable

## Full-paper rule

When the user requests a complete manuscript, do not return an abbreviated pseudo-paper merely to fit a generic page count. Produce a substantively complete draft within the evidence available.

However, completeness never authorizes fabrication. Missing facts must remain marked with the appropriate LXQ placeholders.

## Drafting order

Default production order:

`Results -> Methods -> Discussion -> Introduction -> Abstract -> Title -> declarations/references -> consistency audit`

Use a different order only when the supplied artifact state makes it more reliable.

## Required manuscript qualities

- The Introduction gap matches the actual objective.
- Results are organized by scientific questions and evidence, not software chronology.
- Methods are reproducible and match what was actually done.
- Discussion interprets rather than repeats Results.
- Abstract and Title are written from the final supported argument.
- Claim strength does not exceed evidence strength.
- Citations are verified for consequential claims.
- Figures/tables and textual claims are mutually consistent.
- Numbers, sample sizes, units, effect directions, and statistical results are consistent across artifacts.

## Durable deliverables when requested

Depending on user request and available tooling, the final bundle may include:

- manuscript DOCX;
- journal-template LaTeX/PDF;
- clean Markdown manuscript;
- figure legends;
- evidence-map TSV;
- figure-storyboard TSV;
- terminology ledger;
- citation audit;
- reproducibility checklist;
- issue register/QC report.

Do not claim a PDF/DOCX or journal-template conformance unless the artifact was actually generated and validated.
