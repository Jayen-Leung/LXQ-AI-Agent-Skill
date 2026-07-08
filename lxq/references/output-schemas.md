# Auditable Output Schemas

Prefer UTF-8 TSV for human-editable registers and JSON for nested metadata. Use stable IDs so revisions remain traceable.

## Review profiles

Run `scripts/scaffold_review.py --profile <profile> --output <directory>`.

| Profile | Files |
|---|---|
| `core` | scope, issues, evidence map, terminology ledger, change log, report |
| `revision` | core + reviewer-response tracker |
| `submission` | core + availability inventory |
| `full` | core + reviewer-response tracker + availability inventory |
| `grant` | core + funding-requirement matrix + aims/work-plan matrix + study-design matrix + customer-facing scheme |
| `literature` | core + literature-evidence matrix + acquired-file manifest |
| `complete` | every table above for an integrated research programme |

An optional `manifest.json` records file provenance and checksums.

## Scope JSON

Record `schema_version`, review date/title, invocation intensity, task modes, artifact tracks, scientific question, study design, endpoint/estimand, cohort, assay, reference/build, core claim, evidence boundary, intended use, primary reader, target journal, available and unavailable artifacts, review boundary, decision, and package readiness.

Allowed invocation intensity values: `light`, `standard`, `strict`, `forensic`, or empty while scope is unresolved.

Allowed readiness values: `ready_to_use`, `conditional`, `needs_author_input`, `blocked`, or empty while work is underway.

## Issue register

Required columns:

| Column | Rule |
|---|---|
| `id` | Stable unique ID such as `DATA-001`, `STAT-002`, `TEXT-003`, or `FIG-004` |
| `severity` | `Blocker`, `Major`, or `Minor` |
| `domain` | Identity, design, data, computation, statistics, text, figure, availability, reproducibility, integrity, or another explicit domain |
| `artifact` | Filename or named artifact |
| `location` | Sheet/cell, line, page, panel, function, sample, record, or section |
| `finding` | Verifiable problem statement |
| `evidence` | Source observation, calculation, log, or cross-reference |
| `impact` | Consequence for validity, interpretation, reproducibility, or presentation |
| `required_action` | Concrete resolution or confirmation needed |
| `status` | `open`, `resolved`, `waived`, or `not-applicable` |
| `verification` | How resolution was or will be checked |

Recommended extension columns: `source_class`, `owner`, and `author_input_needed`. Use source classes `supplied-fact`, `directly-verified`, `inference`, `assumption`, or `unresolved`; use `yes`/`no` for author input.

Do not mark an issue resolved when prose changed but the underlying analysis remains invalid. A waiver must name the risk acceptance and rationale in `verification`.

## Evidence map

Use these columns:

`claim_id`, `exact_claim`, `claim_type`, `source_data`, `analysis`, `result_artifact`, `display_artifact`, `manuscript_location`, `citation_status`, `availability_location`, `support`, `boundary`, `limitation`, `required_change`.

Use support values `supported`, `partial`, `unsupported`, or `not-reviewed`. Trace every abstract conclusion and central discussion claim. A figure is a display artifact, not automatically the numerical source; a metadata-only citation is not verified support.

## Terminology ledger

Use:

`term_id`, `canonical_term`, `variants_found`, `definition`, `unit_or_format`, `first_use`, `applies_to`, `status`, `notes`.

Lock canonical group names, endpoints, assays, identifiers, builds, units, abbreviations, panel labels, and software names. Use status `locked`, `needs-confirmation`, or `deprecated`.

## Change log

Use:

`change_id`, `artifact`, `location`, `change_type`, `before`, `after`, `rationale`, `evidence`, `meaning_changed`, `author_confirmation`, `verification`.

Set `change_type` to `substantive`, `statistical`, `data`, `figure-layout`, `language`, or `formatting`. Use `yes`/`no` for meaning change and author confirmation.

## Reviewer-response tracker

Use:

`comment_id`, `source`, `verbatim_or_faithful_comment`, `category`, `severity`, `proposed_action`, `evidence_needed`, `manuscript_location`, `owner`, `status`, `verification`.

Assign editor items `E.1`, reviewer items `R1.1`, `R1.2`, `R2.1`, and so on. Never claim a change without a real location or explicit `[AUTHOR_INPUT_NEEDED: ...]` placeholder.

## Availability inventory

Use:

`dataset_id`, `description`, `supports_claims`, `data_state`, `access_route`, `repository`, `identifier`, `version`, `license_or_terms`, `restriction_reason`, `access_process`, `metadata_status`, `status`, `verification`.

Allowed access routes: `public-repository`, `controlled-access`, `within-paper-or-supplement`, `reused-public-source`, `third-party-restricted`, `justified-request`, and `not-applicable`.

## Funding-requirement matrix

Use:

`requirement_id`, `source`, `official_requirement`, `category`, `proposal_location`, `status`, `owner`, `verification`.

Use the current official call and template as the source. Typical categories include eligibility, scientific content, format, page/word limit, budget, attachments, ethics, data management, deadline, and submission-system fields.

## Grant aims and work-plan matrix

Use:

`aim_id`, `question_or_hypothesis`, `rationale`, `preliminary_evidence`, `design`, `experimental_unit`, `primary_outcome`, `analysis`, `success_criterion`, `dependency`, `risk`, `alternative`, `deliverable`, `milestone`, `owner`, `timing`, `budget_link`, `status`.

Do not use planned work as preliminary evidence. Each aim must have a useful contingency and a traceable relationship to personnel, timing, and budget.

## Grant study-design matrix

Use:

`component_id`, `aim_id`, `research_object`, `setting`, `study_design`, `experimental_unit`, `sample_size`, `sample_size_basis`, `groups_and_controls`, `inclusion_criteria`, `exclusion_criteria`, `primary_endpoint`, `secondary_endpoints`, `timepoints`, `biospecimens_or_data`, `detection_indicators`, `wet_lab_methods`, `data_source`, `bioinformatics_algorithms`, `validation_strategy`, `statistical_methods`, `missing_data_and_multiplicity`, `planned_visuals`, `expected_result`, `success_criterion`, `budget_link`, `status`, `notes`.

Use one row per coherent design component or aim. Use `not-applicable` only when the field genuinely does not apply; do not use it to hide an undecided design. A final row must not leave sample size, inclusion/exclusion criteria, endpoints, detection indicators, statistics, or validation empty.

## Customer-facing scheme

Use `customer-scheme.md` for the directly readable delivery. Unless an official funding template requires another order, include the 14-section Chinese structure from `references/medical-research-delivery-zh.md` plus references. Each research-content item must identify the research object, method, indicator, and expected judgment. Keep provisional claims visibly marked with `建议`, `拟采用`, `计划`, `需进一步确认`, or an LXQ placeholder.

## Literature evidence matrix

Use:

`paper_id`, `citation`, `doi_or_id`, `article_type`, `review_question`, `population_or_model`, `design`, `sample_size`, `exposure_or_intervention`, `comparator`, `outcome`, `effect_and_uncertainty`, `main_claim`, `support_grade`, `bias_or_limitation`, `source_anchor`, `full_text_status`, `notes`.

Allowed support grades: `strong`, `partial`, `background`, `contradictory-or-limiting`, `metadata-only`, and `not-assessable`.

## Acquired-literature file manifest

Use:

`paper_id`, `title`, `doi`, `pmid`, `pmcid`, `arxiv_id`, `version`, `source_url`, `access_route`, `license_or_status`, `retrieved_date`, `filename`, `size_bytes`, `sha256`, `identity_verified`, `notes`.

Use `yes`/`no` for identity verification. Allowed access routes are `user-provided`, `institution-authorized`, `publisher-open-access`, `pubmed-central`, `preprint-repository`, `institutional-repository`, `library-document-delivery`, and `metadata-only`. Record `full_text_unavailable` in status/notes instead of attempting to bypass access controls.

## Decision consistency

- `FAIL`: unresolved blocker, invalid central analysis, or insufficient evidence/provenance for the requested decision.
- `CONDITIONAL PASS`: no unresolved blocker, but major issues or prerequisites remain.
- `PASS`: all applicable gates resolved or explicitly waived, with no unresolved blocker or major issue.

Decision and readiness are separate. A scientifically valid analysis may still be `needs_author_input` for submission metadata; a polished package may still `FAIL` scientifically.

## Validation

```powershell
python scripts/validate_issue_register.py issue-register.tsv
python scripts/validate_review_bundle.py <bundle-directory> --profile full
python scripts/validate_literature_files.py <bundle-directory>/literature-files.tsv
python scripts/validate_grant_delivery.py <bundle-directory>
```

Validators return exit code 2 for schema/content errors. The issue validator returns exit code 3 when an unresolved issue meets `--fail-on`.
