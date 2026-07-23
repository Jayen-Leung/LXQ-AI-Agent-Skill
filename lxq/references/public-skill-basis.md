# Public Skill Design Basis

This file records the public and user-supplied skill sources consulted for LXQ's reusable design patterns. It is not a substitute for primary scientific guidelines or current tool documentation.

## Sources

- OpenAI Skills Catalog: `https://github.com/openai/skills` (individual skills carry their own licenses). Design patterns used: concise routing, progressive disclosure, deterministic helper scripts, explicit validation, and clear output conventions.
- GPTomics bioSkills: `https://github.com/GPTomics/bioSkills` (MIT License, copyright GPTomics). Design patterns used at a conceptual level: stage-specific assay routing, installed-version checks, explicit ownership boundaries, common-error tables, stage order, and machine-readable QC aggregation.
- Installed Nature skill suite (`nature-writing`, `nature-polishing`, `nature-figure`, `nature-response`, `nature-reviewer`, `nature-data`, and `nature-citation`; inspected 2026-06-30). Design patterns used: manifest-driven conditional loading, always-loaded core contracts, fact-base and claim/evidence/boundary alignment, terminology ledgers, targeted revision loops, stable reviewer-comment IDs, author-input placeholders, data-access routing, separate readiness states, and final QA contracts.
- Installed `nature-reader` and `nature-academic-search` skills (inspected 2026-07-08). Design patterns used: source-format and workflow routing, stable block anchors, figure/table-aware reading, exact search logging, source reliability tiers, deduplication, identifier conversion, and reference-manager exports.
- Anthropic `doc-coauthoring` skill: `https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring` (repository license applies). Design patterns used conceptually: context gathering, section-by-section surgical refinement, and fresh-reader testing.
- Community `grant-writer` skill from `majiayu000/claude-skill-registry` (MIT, inspected 2026-07-08). Design patterns used conceptually: sponsor alignment, measurable objectives, evaluation plan, capacity, sustainability, and budget-to-activity mapping.
- User-supplied `Medical Research Delivery Skill` specification (received 2026-07-08). Requirements incorporated: client-facing topic selection, fixed proposal structure, wet-lab and bioinformatics detail, sample size and endpoint completeness, budget/background fit, uncertainty labelling, and a direct-readability completion gate.
- User-supplied Kimi `sci-paper-cn` specification and its Structure & Narrative, Visual Style & Typography, and Figures/Tables/Equations contracts (received 2026-07-23). Patterns adapted: contract-based manuscript planning, funnel narrative, paragraph jobs, forward references, figure/table completeness, self-contained captions, and submission-aware presentation. CVPR/ResNet-specific fixed section hierarchy, fixed page budgets, universal double-column typography, mandatory Related Work, and computer-science table conventions were not adopted as biomedical defaults.

## Adaptation policy

- Use public skills to identify workflow patterns and failure modes; verify consequential scientific claims against primary literature, official tool documentation, protocols, or domain standards when acting on real data.
- Do not treat a repository's popularity, benchmark claim, or polished output as evidence of scientific correctness.
- Record versions or retrieval dates when a task depends on evolving software behavior.
- Avoid copying large passages or code examples. Keep LXQ focused on cross-artifact audit, repair, integrity, evidence linkage, and manuscript architecture rather than duplicating assay-specific tool manuals.
- Keep all LXQ `always_load` paths inside the LXQ directory so the skill remains portable and does not depend on sibling `_shared` folders.
- When adapting a domain-specific writing skill to biomedical work, preserve reusable workflow logic but replace venue-specific assumptions with study-type, evidence-strength, reporting-guideline, and target-journal routing.
