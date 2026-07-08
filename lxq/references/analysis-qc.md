# Analysis QC Reference

## Contents

1. Universal intake
2. Design and statistics
3. Assay-specific checks
4. Reproducibility
5. Failure conditions

## Universal intake

Capture:

- Scientific question, primary and secondary endpoints, planned contrasts, and intended inference.
- Cohort source, inclusion/exclusion rules, biological versus technical replicates, pairing, repeated measures, and sample attrition.
- Data lineage from source files to final outputs, including checksums when practical.
- Assay platform, library preparation, reference genome/build, gene annotation release, transcript model, database versions, and identifier namespace.
- Units, encoding, missing-value conventions, batch variables, clinical covariates, and de-identification status.

Check that IDs are unique where expected and consistent across metadata, matrices, alignments, manifests, figures, and manuscript counts. Detect swaps, duplicates, impossible dates or values, mixed genome builds, and silent coordinate conversion.

Classify every input as raw, filtered, normalized, transformed, integrated, imputed, or presentation-only. Record the assay stage and expected predecessor artifacts. A valid-looking downstream object does not prove that upstream cell calling, alignment, quantification, or filtering was correct.

For consequential thresholds, record whether each is a hard-validity rule, protocol value, cohort-relative rule, heuristic convention, or exploratory choice. Show attrition and perform sensitivity checks when a threshold could change the conclusion.

## Design and statistics

- Define the experimental unit; do not treat cells, reads, tiles, or repeated observations as independent biological replicates.
- Check randomization, blinding, controls, balance, center/site effects, sex and age handling, batch-confounding, and information leakage.
- Distinguish confirmatory from exploratory analyses. Identify post hoc thresholds and outcome-informed exclusions.
- Report effect sizes and uncertainty, not significance alone.
- Match the model to distribution, dependence, censoring, repeated measures, zero inflation, overdispersion, compositionality, and sampling design.
- Correct multiplicity across the actual family of tested hypotheses; state the method and denominator.
- Inspect model diagnostics and influential observations. Use sensitivity analyses for consequential assumptions.
- Keep prediction performance separate from biological association. Require leakage-safe splits, nested tuning when applicable, calibration, and external validation claims only when truly external.
- Avoid causal language without a defensible causal design and assumptions.

## Assay-specific checks

### Bulk RNA-seq

- Verify FASTQ quality, adapters, duplication, contamination, mapping or pseudoalignment rate, strandedness, rRNA content, gene-body coverage, sample correlation, PCA, and library size.
- Use raw counts for count-based differential expression; do not use TPM/FPKM as DESeq2 input.
- Build a design formula that reflects pairing, batch, and covariates. Confirm full rank and valid contrasts.
- Inspect low counts, dispersion, outliers, independent filtering, shrinkage method, effect direction, and FDR.
- Treat pathway analysis as dependent on the tested gene universe, identifier mapping, ranking method, database version, and redundancy handling.
- Infer strandedness empirically before quantification when possible. In non-UMI RNA-seq, do not remove coordinate duplicates reflexively; high expression can produce legitimate duplicate coordinates.

### Single-cell and spatial omics

- Retain sample/donor identity and avoid pseudoreplication. Prefer donor-level inference or justified mixed/pseudobulk models.
- Inspect counts/features, mitochondrial and ribosomal fractions, ambient RNA, doublets, empty droplets, cell-cycle effects, dissociation stress, and per-sample retention.
- Set QC thresholds per dataset or sample using distributions and biology; do not copy universal cutoffs blindly.
- Separate normalization, integration, visualization, clustering, and differential testing. Do not use corrected embeddings as expression values.
- Demonstrate that integration reduces technical variation without erasing biological structure.
- Support annotation with multiple markers, negative markers, reference evidence, tissue context, and uncertainty; avoid circular marker validation.
- For spatial data, check tissue coverage, spot/cell segmentation, registration, spatial autocorrelation, and resolution-dependent claims.
- For droplet data, preserve the unfiltered matrix. Perform cell calling, ambient-RNA assessment, adaptive QC, and doublet handling per capture/sample before merging; retain raw counts separately from normalized or integrated layers.
- Treat fixed mitochondrial, feature, or count cutoffs as tissue- and platform-dependent heuristics. Inspect the biological identities removed by filtering, not only the surviving UMAP.

### WES/WGS and variants

- Record build, capture kit, read group, alignment, duplicate handling, coverage breadth/depth, contamination, sex check, relatedness, and tumor-normal pairing where applicable.
- Normalize and decompose variants before comparison. Verify REF alleles and liftover provenance.
- Record caller, version, parameters, filtering strategy, callable territory, allele balance/VAF, strand bias, depth, and artifact context.
- Distinguish germline, somatic, mosaic, CNV, and structural-variant evidence.
- Treat ClinVar, gnomAD, COSMIC, ACMG/AMP, and therapeutic annotations as versioned evidence requiring qualified review; verify transcript and HGVS nomenclature.

### Proteomics and metabolomics

- Check identification and quantification FDR, decoys, contaminants, missingness mechanism, normalization, batch drift, internal standards, pooled QC, carryover, and feature annotation confidence.
- Distinguish imputation for visualization from inferential use. Test sensitivity to imputation and filtering.
- Record search database, digestion, modifications, mass tolerances, software versions, and metabolite identification level.
- Inspect raw intensity, identification counts, contaminants/decoys, and injection or batch drift before normalization can hide loading failures. Compute conventional CV on the linear scale or explicitly use an appropriate geometric formulation for log data.

### Microbiome and compositional data

- Check negative controls, extraction and sequencing batches, read depth, contamination, host filtering, taxonomic database/version, prevalence filtering, and rare taxa.
- Respect compositionality; avoid interpreting relative abundance as absolute change without supporting measurements.
- Justify normalization, zero handling, distance metric, covariate model, and multiple-testing procedure.

### Clinical and observational data

- Verify eligibility, index date, follow-up, censoring, missingness, outcome adjudication, unit harmonization, coding dictionaries, and cohort attrition.
- Prevent immortal-time, selection, collider, and data-leakage biases.
- Predefine confounders where possible; document propensity, weighting, matching, survival, and competing-risk assumptions.

## Reproducibility

Require enough material to reconstruct the result:

- Immutable source-data references and a manifest.
- Script or workflow entry point and execution order.
- Locked environment or container, software and database versions, reference files, parameters, seeds, and hardware-sensitive nondeterminism.
- Logs, session information, intermediate checkpoints, and a clean rerun when feasible.
- Separation of source data, derived data, code, and final outputs.
- Verification of the installed tool/API version and the actual command help or function signature before reusing a public example.
- An expected sample roster reconciled against files and aggregated QC reports. MultiQC and similar tools summarize discovered outputs; a missing sample or empty module is not a pass.

## Failure conditions

Return `FAIL` or a blocker when any of these affects the central analysis:

- Unresolved sample/group identity, mixed reference builds, corrupted or undocumented source data.
- Biological replication replaced by technical replication or cells/reads.
- Outcome leakage, invalid contrast, non-identifiable model, or statistics that cannot be traced to data.
- Selective deletion or undisclosed exclusion that changes conclusions.
- Results only available as screenshots or prose with no traceable table/code when numerical validation is requested.
- Clinical or variant interpretation presented as definitive without required evidence and qualified review.
