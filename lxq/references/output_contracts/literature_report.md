# Literature Report Output Contract

Use `standard` for a focused single-paper reading report and `strict` for a formal evidence audit or multi-paper synthesis.

## Single-paper Chinese reading report

When the user asks for a directly readable Chinese literature report, especially when a PDF or full text is supplied, produce a structured report rather than a loose abstract summary. The default section order is:

1. English article title.
2. Chinese translated title.
3. Bibliographic metadata table: journal, publication date, DOI/PMID/PMCID when verified, article type, model or population, and full-text status.
4. Core conclusion box: one bounded paragraph stating the central mechanism or advance, the evidence basis, and the main boundary.
5. Research background and unresolved problem.
6. Research question or hypothesis.
7. Overall study design and technical route.
8. Main results, organized in the paper's evidentiary order. Each result subsection must contain:
   - the question addressed;
   - model, intervention, comparator, and key method;
   - principal finding with quantitative information when available;
   - interpretation calibrated to the evidence;
   - the corresponding figure or table placed nearby when lawful and technically feasible.
9. Mechanistic evidence chain, preferably as a compact 2x2 matrix when four linked steps are present.
10. Innovation and contribution, separated into conceptual, methodological, and translational value only when supported.
11. LXQ evidence-strength matrix with columns `证据环节 / LXQ支持等级 / 主要依据 / 边界`.
12. Methodological limitations and uncertainty.
13. Future experiments or research directions, limited to actions that follow from identified gaps.
14. Article-use boundary table: `可直接支持 / 需要限定 / 不宜外推`.
15. Final reading conclusion.

Use prose paragraphs rather than keyword dumps. Keep gene and protein symbols, pathway names, statistics, doses, time points, model names, and figure numbers exact. Distinguish author claims, directly demonstrated findings, reasonable inference, and unsupported extrapolation.

## Figures and source grounding

- Use the user-supplied or lawfully acquired full text as the primary source.
- Place each figure or table near the first substantive result paragraph that interprets it.
- Use a tight crop rather than a full-page screenshot when possible.
- Preserve the source figure number and provide a Chinese title plus a short evidence-location/source note.
- State whether the visual is unchanged, cropped, scaled, translated, redrawn, or recombined.
- Do not infer measurements from an image when the paper does not report them.

## Word and PDF delivery

When the user asks for Word, PDF, a formal deliverable, or says to use the established LXQ literature-report format, load `references/literature-report-word-style-zh.md` and follow it. Generate a DOCX first and render every page for visual inspection before delivery. A PDF may be exported as a companion file when requested or useful. Preserve the editable Word file as the primary deliverable.

## Evidence-audit fields

For strict reports or multi-paper synthesis, also return the review question, search scope and date, exact query or its location, selection boundary, study evidence matrix, stable source anchors, effect and uncertainty, bias or limitation, contradictory evidence, support grade, full-text status, and lawful acquisition provenance.

Do not call an informal search systematic, treat metadata as full-text evidence, imply unavailable papers were read, or certify a mechanistic or clinical claim beyond the supplied evidence.