# Invocation Intensity

LXQ supports four invocation intensity levels.

## light

Use for quick topic screening, brief feasibility judgment, early-stage client-facing direction suggestions, short method comments, and quick refinement.

Do not create full evidence ledgers, structured review bundles, issue registers, or exhaustive QC reports unless the user explicitly requests them.

Typical triggers:

- “给我几个方向”
- “选三个最好的”
- “简单判断一下可行性”
- “售前初步思路”
- “这个方向能不能做”

## standard

Use for complete customer delivery schemes, fund pre-application content, grant rationale, research objectives, research contents, wet experiment plans, bioinformatics workflows, and literature-based project design.

Typical triggers:

- “完整内容”
- “客户直接看”
- “交付版本”
- “正式一点”
- “写成申报书结构”
- “导出为 Word 的内容”

## strict

Use for formal grant/manuscript/submission audits, statistical QC, figure QC, reproducibility review, data availability review, and revision package inspection.

Typical triggers:

- “审核”
- “投稿前检查”
- “返修”
- “数据一致性”
- “图表是否有问题”
- “统计是否合理”

## forensic

Use when sample identity, image integrity, data provenance, research misconduct risk, clinical claim validity, or raw data authenticity is questioned.

Typical triggers:

- “是否造假”
- “样本是否对得上”
- “原始数据是否支持”
- “图像是否被处理”
- “结果是否可信”

## Default routing

- If the user asks for early directions or topic suggestions, default to `light`.
- If the user asks for a complete customer-facing or fund-facing deliverable, default to `standard`.
- If the user asks for audit, revision, submission, statistics, figure, or reproducibility checks, default to `strict`.
- If the user asks about authenticity, provenance, manipulation, or research integrity, default to `forensic`.
- Use the lowest intensity that safely satisfies the request. Increase intensity when evidence risk or requested assurance increases; never reduce scientific integrity rules.
