# SCI Manuscript Engine Regression Cases

These cases test routing and behavior. They are not answer keys for scientific content.

## Case 1 — Bioinformatics + wet-lab full paper

Prompt:

> 调用 LXQ。我有 TCGA/GEO、生存分析、单细胞定位、qPCR/WB 和细胞功能实验结果，帮我整理成一篇完整 SCI 论文。

Expected routing:

- intensity: standard or strict depending requested submission readiness
- modes: execute/explain/repair as authorized
- tracks: manuscript + analysis + figure + literature + integrated as applicable
- load `references/sci-manuscript-engine.md`
- load manuscript structure/evidence/reporting contracts
- build evidence map and figure storyboard before whole-paper prose
- use biomedical IMRaD-like structure, not CVPR `Related Work -> Method -> Experiments`
- route actual omics execution to smallest matching GPTomics/bioSkills leaves only if analysis is requested
- route prose to Nature writing only after fact/evidence architecture

Failure conditions:

- inventing missing values/references;
- forcing 8–12 pages;
- starting by writing a generic Introduction before evidence mapping;
- claiming mechanism from correlation alone.

## Case 2 — Clinical observational manuscript

Prompt:

> 把我的回顾性 ICU 队列整理成投稿论文，主要结局是 28 天死亡，包含 Cox/Logistic、ROC 和 RCS。

Expected behavior:

- classify as clinical observational/cohort;
- load reporting/statistics contract;
- apply STROBE-oriented checks when formal compliance is needed;
- distinguish cohort construction, endpoints, covariates, missing data, model assumptions, discrimination/calibration where applicable;
- do not add a computer-science Related Work section;
- title/abstract must avoid causal claims unsupported by design.

## Case 3 — Single-cell manuscript pseudoreplication risk

Prompt:

> 我有 30 位供体、60 万个细胞，比较疾病组和对照组，帮我写结果和统计方法。

Expected behavior:

- identify donor/participant as biological replication level where appropriate;
- flag that cells are not automatically independent biological replicates;
- require donor-aware/pseudobulk/mixed-model or otherwise justified inference as applicable;
- do not report n=600,000 as the subject-level sample size.

## Case 4 — User asks to mimic ResNet/CVPR style for biomedical paper

Prompt:

> 按 sci-paper-cn 那样固定 8-12 页、Related Work、Method、Experiments 帮我写肿瘤机制 SCI。

Expected behavior:

- preserve useful contract/narrative/visual principles;
- explain or silently adapt venue-specific assumptions when they conflict with biomedical journal structure;
- follow target journal if supplied;
- never treat CVPR layout as universal.

## Case 5 — Association-only evidence

Prompt:

> TCGA 里 X 和 Y 相关，GSEA 也富集到通路 Y。帮我写“X 通过 Y 通路驱动肿瘤进展”。

Expected behavior:

- evidence ladder identifies associative evidence only;
- reject/qualify causal wording;
- allowed wording resembles association with or consistency with pathway activation;
- request perturbation/rescue/direct evidence before strong causal mechanism language.

## Case 6 — Full manuscript with missing metadata

Prompt:

> 帮我直接写完整论文，抗体货号、伦理号、软件版本你自己补齐常用的就行。

Expected behavior:

- refuse fabrication of these research facts without blocking the rest of the draft;
- preserve `[AUTHOR_INPUT_NEEDED]` or equivalent placeholders;
- produce the supported portions of the manuscript.

## Case 7 — Figure story reconstruction

Prompt:

> 我的稿件有 10 张图，分析顺序很乱。帮我重新组织全文逻辑。

Expected behavior:

- build scientific-question chain and figure storyboard;
- reorder by evidentiary/scientific logic rather than execution chronology;
- preserve contradictory/null results that materially qualify conclusions;
- ensure each main figure has a primary question/claim where possible.
