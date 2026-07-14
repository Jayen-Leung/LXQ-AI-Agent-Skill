# Specialist skill routing

Use this table after LXQ has fixed scope, authorization, evidence boundaries, and the research fact base. Select the smallest set that covers the task. Do not load all specialists by default.

| Task signal | Select | Typical sequence |
|---|---|---|
| Draft or restructure manuscript sections from claims, results, figures, or notes | `nature-writing` | evidence base -> writing -> LXQ consistency check |
| Polish or translate already drafted academic prose; repair LaTeX layout | `nature-polishing` | evidence lock -> polishing -> meaning-drift check |
| Create, revise, audit, or polish scientific figures | `nature-figure` | conclusion/evidence definition -> figure -> LXQ numerical and provenance QA |
| Answer editor or reviewer comments point by point | `nature-response` | comment ledger -> evidence check -> response -> propagation check |
| Add strict Nature/CNS citations to supplied prose | `nature-citation` | claim segmentation -> scoped search -> citation insertion -> support check |
| Broad or multi-source literature search, citation verification, MeSH, or citation-file work | `nature-academic-search` | search plan -> retrieval -> deduplication -> evidence synthesis |
| Full-paper bilingual reading, translation, figure/table placement, or source anchors | `nature-reader` | lawful source acquisition -> anchored reading -> synthesis |
| Data Availability statement, repository plan, dataset citation, or FAIR metadata | `nature-data` | artifact inventory -> repository/access checks -> statement -> LXQ readiness |
| Independent pre-submission reviewer-perspective assessment | `nature-reviewer` | freeze authoring context -> independent review -> LXQ cross-artifact synthesis |

## Combination rules

- Literature-grounded manuscript drafting: `nature-academic-search` -> `nature-reader` when full papers matter -> `nature-writing` -> `nature-citation` -> `nature-polishing`.
- Manuscript revision: `nature-response` -> `nature-writing` for substantive section changes -> `nature-citation` when support changes -> `nature-polishing` -> LXQ propagation check.
- Figure-led paper work: `nature-figure` before `nature-writing` when the figure defines the claim; otherwise lock manuscript claims before figure revision.
- Pre-submission package: complete authoring first, then use `nature-reviewer` as an independent assessment. Do not use reviewer output as evidence for the paper.
- Availability work: use `nature-data` after the data/code inventory is real; unresolved accessions remain explicit placeholders.

## Invocation and fallback

1. Announce the selected specialists and why when user-visible scope correction is useful.
2. Prefer an installed skill with the exact name.
3. If unavailable, load `bundled_skills/<skill-name>/SKILL.md` completely and follow its referenced files relative to that bundled directory.
4. If required tools or sources remain unavailable, use the specialist's documented fallback and list unfinished work. Never fabricate invocation, searches, citations, figures, reviews, or validation.
5. LXQ remains responsible for evidence linkage, terminology, numerical consistency, provenance, integrity, and final readiness.
