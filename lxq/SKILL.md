---
name: lxq
description: Audit, repair, execute, and document medical, clinical, and bioinformatics research with evidence-linked quality control across raw data, omics pipelines, statistics, manuscripts, grant and research proposals, customer-facing medical research schemes, pre-sales research content, literature search and lawful full-text acquisition, paper reading and evidence synthesis, reviewer revisions, data or code availability, tables, and scientific figures. Use whenever the user says LXQ or asks for LXQ-assisted work; also use for hospital, department, or client research planning; funding calls, budgets, topic selection, study aims, wet-lab or bioinformatics plans; bulk or single-cell RNA-seq, spatial omics, WES or WGS, proteomics, metabolomics, microbiome, clinical research, reproducibility, manuscript revision, reviewer responses, figure integrity, submission readiness, or cross-artifact research audits.
---

# LXQ Research Quality Control — Router

LXQ uses a Nature-inspired layered design:

- `static/core/` contains the stance, workflow, and output contract loaded for every LXQ task.
- `manifest.yaml` detects task modes and artifact tracks, then loads only the relevant fragments and references.
- `references/` contains deeper analysis, manuscript, figure, submission, and output-schema guidance.

Do not apply LXQ from this router alone. Load the declared files before acting.

For a complete Chinese capability inventory or internal audit, read `references/lxq-functions-v2.5-zh.md`. Treat it as an audit map; the executable scripts and routed source references remain the implementation source of truth.

## Routing protocol

Use this order: identify task intent -> identify invocation intensity -> identify task mode -> identify functional tracks -> load the corresponding rules.

### 1. Load the manifest and core

Read [manifest.yaml](manifest.yaml), then read every file under `always_load` in the listed order.

### 2. Detect invocation intensity

Select exactly one level from `light`, `standard`, `strict`, or `forensic`, using `static/fragments/invocation_intensity.md`.

- `light`: quick topic screening, brief feasibility judgment, or short refinement. Do not expand into a full QC bundle unless requested.
- `standard`: complete customer-facing, fund-facing, methodological, or literature-based deliverables.
- `strict`: formal grant, manuscript, submission, statistical, figure, reproducibility, or availability audits.
- `forensic`: authenticity, provenance, manipulation, raw-data integrity, sample identity, or misconduct-risk questions.

Invocation intensity controls depth and artifact volume. It never relaxes evidence, privacy, safety, or non-fabrication rules.

### 3. Detect task modes

Select one or more `task_mode` values:

- `audit`: diagnose and grade supplied work without silently changing it.
- `repair`: correct verified defects while preserving originals and author intent.
- `execute`: run or rebuild an analysis from supplied artifacts with reproducible steps.
- `explain`: interpret evidence, limitations, or methods without implying unperformed validation.

### 4. Detect artifact tracks

Select every applicable `artifact` value:

- `analysis`: data, code, pipelines, matrices, FASTQ/BAM/VCF, AnnData/Seurat, or statistics.
- `manuscript`: manuscript prose, tables, supplements, methods, results, or consistency review.
- `figure`: plots, multi-panel figures, microscopy, pathology, gels/blots, flow, or legends.
- `revision`: editor letters, reviewer comments, rebuttals, tracked changes, or revision packages.
- `availability`: data/code/materials availability, repositories, accessions, or FAIR metadata.
- `grant`: funding calls, research proposals, specific aims, work packages, milestones, evaluation plans, budgets, or funder-facing narratives.
- `delivery`: Chinese customer-facing medical research schemes, topic shortlists, pre-sales content, hospital or department research planning, and directly readable proposal drafts.
- `delivery-en`: the English-language version of the same customer-facing workflow.
- `literature`: literature search, lawful full-text acquisition, PDF/HTML reading, figure/table analysis, citation verification, or evidence synthesis.
- `integrated`: a complete project, manuscript, or submission spanning multiple artifact types.

State the detected modes and tracks in one short line when doing so helps the user correct scope cheaply.

### 5. Detect style overlays

For Chinese customer delivery, grant proposals, research backgrounds, objectives, research contents, and innovation sections, load `static/fragments/style/anti_ai_zh.md` by default.

### 6. Load only matching material

Read the fragment/reference mapped to every selected value. Do not load unrelated tracks. For `integrated`, also load the component tracks actually present.

Load exactly one primary task output contract from `references/output_contracts/` when a matching contract exists. Invocation intensity determines depth: a light direction request must not inherit the strict audit-report shape.

### 7. Run the core workflow

Follow `static/core/workflow.md` end to end. Use the loaded mode fragments to control what may change and the loaded artifact references to determine domain checks.

For specialized production work, route after establishing the LXQ fact base:

- `nature-writing` / `nature-polishing` for manuscript construction or language.
- `nature-figure` for data-derived manuscript figures.
- `nature-response` for point-by-point reviewer responses.
- `nature-citation` / `nature-academic-search` for citation support and verification.
- `nature-reader` for source-grounded full-paper reading, translation, figures/tables, and stable source anchors.
- `nature-data` for availability statements and repository planning.
- `nature-reviewer` for an independent reviewer-perspective assessment.
- `documents:documents` / `pdf:pdf` for layout-sensitive files.

For Chinese customer-facing medical research delivery, read `references/medical-research-delivery-zh.md`. For an explicitly English deliverable, read `references/medical-research-delivery.md`. Do not load both unless comparing language versions. Produce the directly readable scheme first, then keep assumptions, missing facts, compliance items, and validation evidence visible in the accompanying registers.

LXQ remains responsible for evidence linkage, numerical consistency, provenance, integrity, and readiness boundaries across routed work.

When an external skill or tool is unavailable, do not claim it was invoked or completed. Provide a text-level fallback when possible, list unfinished work explicitly, and provide copyable content or a structured draft when DOCX, PDF, PPT, or figure generation is unavailable. LXQ still owns evidence boundaries, numerical consistency, research integrity, and readiness decisions.

### 8. Validate before delivery

When a durable audit is useful:

- Run `scripts/scaffold_review.py` with the appropriate profile.
- Run `scripts/build_manifest.py` for file provenance.
- Run `scripts/validate_issue_register.py` on the issue register.
- Run `scripts/validate_review_bundle.py` on the complete bundle.
- Run `scripts/validate_literature_files.py` when full-text files were acquired.
- Run `scripts/validate_grant_delivery.py` before calling a customer-facing medical research scheme complete.
- Run `scripts/score_delivery_quality.py` for a Chinese customer-delivery quality score.
- Run `scripts/score_grant_quality.py` for a Chinese grant quality score.
- Run `scripts/validate_eval_cases.py eval_cases` before a regression run or release.

The grant-delivery validator defaults to Chinese headings. Use `--language en` only for an English customer scheme.

Conclude only within the reviewed scope. Never imply clinical validity, editorial acceptance, or review of unavailable artifacts.

During LXQ maintenance or evaluation, use `examples/` for transferable positive and negative behavior patterns and `eval_cases/` for held-out regression cases. Do not expose expected answers to the system being evaluated.
