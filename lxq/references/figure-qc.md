# Scientific Figure QC Reference

## Contents

1. Evidence class
2. Universal checks
3. Permitted and prohibited edits
4. Image-specific checks
5. Export and accessibility

## Evidence class

Classify every panel:

- Quantitative plot generated from data.
- Raw or processed evidentiary image such as microscopy, pathology, radiology, gel, blot, or flow plot.
- Derived map, embedding, heatmap, segmentation, or model output.
- Conceptual schematic or illustration.

Require stronger provenance and edit restrictions for evidentiary panels than for illustrations.

Before plotting or redesigning, establish a figure contract: one-sentence conclusion, evidence chain, unique job of each panel, figure archetype, final dimensions/formats, statistical requirements, source-data mapping, and review risks. Drop panels that carry no unique evidence. Aesthetic polish remains subordinate to the claim the figure must defend.

## Universal checks

- Verify panel-to-source mapping, sample/group labels, biological replicate count, units, scales, transformations, normalization, and statistical annotations.
- Match plotted values to result tables or regenerate from source data.
- Show uncertainty and individual observations when appropriate; disclose what error bars represent.
- Avoid truncated axes, area/volume encodings that exaggerate differences, incompatible scales, rainbow maps, overplotting, and hidden missing data.
- Define abbreviations, symbols, thresholds, tests, multiple-testing correction, `n`, and whether `n` means participants, samples, experiments, cells, reads, or images.
- Keep colors and group order consistent across the manuscript.
- Confirm legends describe what is actually shown, including representative-image selection and replication.

## Permitted and prohibited edits

Generally permitted with disclosure when relevant:

- Uniform global brightness/contrast or color balance that does not clip or suppress features.
- Resizing, lossless format conversion, panel alignment, typography, accessible color replacement, and whitespace adjustment.
- Cropping that preserves context and does not remove relevant controls; retain uncropped originals.
- Explicitly described, scientifically justified denoising or background correction applied consistently.

Prohibited for evidentiary images:

- Adding, deleting, moving, cloning, duplicating, or generatively reconstructing features.
- Selective enhancement or local contrast changes that alter interpretation.
- Splicing lanes, fields, or time points without clear separators and disclosure.
- Reusing one image to represent different samples or conditions.
- Hiding saturation, artifacts, controls, negative results, scale bars, or inconvenient regions.
- Changing aspect ratio or interpolation in a way that changes morphology or apparent resolution.

Maintain an edit log containing source filename, output filename, software/version, operation, parameters, scope, reason, and operator/date.

## Image-specific checks

### Microscopy and pathology

- Preserve raw files and metadata; verify objective, magnification, pixel size, channels, exposure, stain, scale bar, and field-selection rule.
- Apply identical acquisition and processing settings across compared groups where feasible; disclose exceptions.
- Avoid claiming cellular or pathological identity beyond available markers and qualified interpretation.

### Gels and blots

- Retain uncropped originals, molecular-weight markers, loading controls, exposure information, lane identity, and replicate provenance.
- Mark splices explicitly and ensure compared bands come from compatible exposures and processing.
- Check saturation and background subtraction; do not use contrast to erase bands.

### Flow cytometry

- Preserve gating hierarchy, compensation/unmixing information, controls, transformations, event counts, and sample-level replication.
- Do not present pooled events as independent biological replicates.

### Embeddings, heatmaps, and omics plots

- Treat UMAP/t-SNE geometry as visualization, not metric evidence beyond justified local structure.
- Record seeds and parameters; color by batches and samples as well as biological labels.
- State scaling, clustering distance/linkage, row/column selection, gene universe, clipping, and color-map midpoint.
- Verify volcano, forest, survival, enrichment, and trajectory plots against underlying numerical outputs.

## Export and accessibility

- Prefer vector PDF/SVG for plots and lossless TIFF/PNG for raster evidence, subject to journal requirements.
- Check final physical dimensions, effective resolution, embedded fonts, line widths, panel labels, and readability at publication size.
- Use colorblind-safe palettes and redundant encodings when color carries meaning.
- Inspect the exported file, not only the plotting window; verify no clipping, font substitution, transparency, or rasterization errors.
- When production is routed to `nature-figure`, respect its explicit Python-or-R backend gate and use the selected backend consistently for drawing, previewing, exporting, and visual QA.
