# LXQ Research Quality Control Skill

[简体中文](#简体中文) · [English](#english)

## 简体中文

LXQ 是面向医学、临床、生物信息学与科研论文生产的 Codex Skill，提供证据关联的审核、修复、执行、科研叙事重构和交付流程。当前版本为 [`2.9.0`](VERSION)。

### 主分支最新更新

[生物医学图像分析指南](lxq/references/biomedical-image-analysis-zh.md) 已加入 LXQ 的按需路由，覆盖荧光与共聚焦显微、组织病理、MRI/CT 和时序图像。指南按图像类型、标注条件和研究终点选择分割、检测或追踪基线，并按受试者、供体或独立实验样本划分数据，检查最终的计数、距离和形态测量误差。

[文献学习笔记](lxq/references/biomedical-image-analysis-literature-zh.md) 收录 55 篇去重文献和 10 篇重点阅读笔记，链接原始论文与补充方法。版本变更记录见 [CHANGELOG.md](CHANGELOG.md)，图像分析更新见 [PR #4](https://github.com/Jayen-Leung/LXQ-AI-Agent-Skill/pull/4)。

### 主要能力

- 医学、生物信息学和多组学数据质量控制
- Bulk RNA-seq、单细胞、空间组学、WES/WGS、蛋白质组、代谢组和微生物组审核
- 临床/观察性研究设计与统计检查
- **SCI Manuscript Engine**：从 Evidence Map、Scientific Story、Figure Storyboard 到完整 manuscript 的证据驱动论文生产
- 按研究类型自动路由临床队列、RCT、诊断/预后、预测模型、生信、单细胞、空间、多组学、湿实验、动物、转化医学及混合型论文结构
- Evidence Ladder（L0-L9）与 claim-strength gate，限制因果/机制表述不超过现有证据强度
- 论文、数字一致性、科学图表和证据图像审核
- 生物医学图像分割、目标检测、时序追踪和图像定量的方法选择与验证
- 审稿回复、投稿包、数据与代码可用性
- 基金课题、研究目标、技术路线、风险和预算审核
- 中文/英文医学科研客户交付方案
- 文献检索、合法全文获取、精读和证据综合
- 中文单篇文献阅读报告：固定内容结构、原文图表就近排布、证据强度矩阵、适用边界和 Word/PDF 交付版式
- 结构化问题清单、证据矩阵、术语台账、Figure Storyboard 和复现清单
- `light`、`standard`、`strict`、`forensic` 四级调用强度
- 中文客户交付去AI味过滤、14段硬结构和预算—技术匹配
- 12个正反示例、33个核心 eval 三件套、7个 manuscript-engine 回归场景和任务输出契约
- 中文客户交付与基金方案启发式质量评分

完整中文功能说明见 [LXQ 中文功能与审核说明](lxq/references/lxq-functions-v2.5-zh.md)。SCI 论文生产总控见 [SCI Manuscript Engine](lxq/references/sci-manuscript-engine.md)。

### 仓库结构

```text
lxq-skill/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── RELEASE_CHECKLIST.md
├── CHANGELOG.md
├── REGRESSION_REPORT.md
├── VERSION
├── .gitignore
├── .gitattributes
├── .github/workflows/validate.yml
├── tests/validate_repository.py
└── lxq/                         # 可直接安装的 Skill 目录
    ├── SKILL.md
    ├── manifest.yaml
    ├── agents/
    ├── static/
    ├── references/
    │   ├── biomedical-image-analysis-zh.md
    │   ├── biomedical-image-analysis-literature-zh.md
    │   ├── sci-manuscript-engine.md
    │   └── manuscript-contracts/
    ├── bundled_skills/             # 九个可独立回退加载的 Nature 专项 skill 源码
    ├── bundled_catalogs/           # GPTomics 与 Orchestra AI Research 技能目录
    └── scripts/
```

### 安装

在仓库根目录执行对应系统的命令。更新已有安装时，先把旧 `lxq` 目录备份到 Skills 目录之外，再执行复制。

**Windows PowerShell**

```powershell
$skillDir = Join-Path $HOME '.codex\skills'
$target = Join-Path $skillDir 'lxq'
if (Test-Path -LiteralPath $target) { throw 'Back up the existing LXQ folder outside the skills directory before installing.' }
New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
Copy-Item -LiteralPath '.\lxq' -Destination $target -Recurse
```

**macOS / Linux**

```bash
skill_dir="$HOME/.codex/skills"
if [ -e "$skill_dir/lxq" ] || [ -L "$skill_dir/lxq" ]; then
  printf '%s\n' 'Back up the existing LXQ folder outside the skills directory before installing.'
else
  mkdir -p "$skill_dir" && cp -R ./lxq "$skill_dir/lxq"
fi
```

安装或更新后，新开一个 Codex 对话以加载最新的 skill 元数据。

### 使用示例

```text
调用 LXQ，审核这个单细胞分析流程并生成问题清单。

调用 LXQ，分析这批共聚焦显微图像。比较细胞核分割方法，按供体留出验证，并报告计数误差。

调用 LXQ，根据科室背景和基金指南筛选三个课题方向，生成客户可直接阅读的中文方案。

调用 LXQ，检索并合法获取相关文献，建立证据矩阵后逐篇精读。

调用 LXQ，按固定文献阅读报告格式总结这篇全文，保留关键结果图，并交付 Word 和 PDF。

调用 LXQ，检查论文、图表、补充材料和审稿回复中的样本量及结论是否一致。

LXQ strict：把这个项目做成一篇可投稿 SCI。
```

完整 SCI 论文任务会优先执行：

```text
Fact Base
→ Study-Type Classification
→ Evidence Map
→ Evidence Strength Grading
→ Scientific Question Chain
→ Figure Storyboard
→ Results
→ Methods
→ Discussion
→ Introduction
→ Abstract
→ Title
→ Citation / Statistics / Figure-Text Consistency
→ Nature Reviewer / Polishing
→ LXQ Final QC
```

推荐调用：

```text
调用 LXQ strict 模式处理本项目。先建立 Evidence Map、Evidence Strength Grading、Scientific Question Chain 和 Figure Storyboard，再按 Results -> Methods -> Discussion -> Introduction -> Abstract -> Title 的内部顺序构建全文。禁止虚构任何数据、统计量、文献、伦理号、基金号、软件版本、试剂货号或未完成实验。
```

### 本地验证

仓库测试只依赖 Python 标准库：

```bash
python tests/validate_repository.py
```

测试内容包括：

- Skill 基本结构和前置元数据
- 路由引用路径存在性
- 十一个 Python 脚本语法和命令入口
- SCI Manuscript Engine、四类 manuscript contracts、完整论文输出契约及路由完整性
- 2026 NSFC 正式申报书 DOCX 模板、五页格式契约和结构验证入口
- 中文文献阅读报告内容契约及 Word 版式路由
- UTF-8 文件完整性
- `core`、`grant`、`literature` 和 `complete` 工作包生成与结构验证
- 中文基金客户交付模板和空文献清单验证
- 中文内部审核文件与 Skill 文件清单一致性
- 33个核心 eval 三件套、7个 manuscript-engine 回归场景、类别配额、rubric字段和评分权重
- 客户交付/基金质量评分器的正负向区分能力

GitHub Actions 会在推送和 Pull Request 时自动执行同一测试。

### 安全与科研边界

- LXQ 不是临床诊疗系统，不替代伦理、统计、遗传、病理、监管或编辑专家审核。
- 不要在公开 Issue、PR、测试或示例中提交患者级数据、受保护健康信息、访问凭据或未公开研究材料。
- 不得虚构数据、引用、伦理批准、数据库编号、前期结果或已经执行的分析。
- 文献全文仅能通过合法、授权的方式获取。
- 结构验证通过不等于科学有效性通过。
- SCI Manuscript Engine 不会把数据库相关性、单一队列结果或探索性分析自动升级为因果机制或临床有效性结论。

详见 [SECURITY.md](SECURITY.md)。

### 上传到 GitHub

在安装 Git 后，于本仓库目录执行：

```bash
git init
git add .
git commit -m "Release LXQ 2.9.0"
git branch -M main
git remote add origin https://github.com/<你的账号>/<仓库名>.git
git push -u origin main
```

也可以在 GitHub 网页创建空仓库后，将本目录内容整体上传。不要只上传压缩包作为仓库内容。

### 发布前必须决定

本仓库当前没有替你选择开源许可证。在公开发布前，请根据是否允许他人复制、修改和商业使用，选择合适的 `LICENSE`；未选择许可证时，默认版权规则通常不授予他人自由复用权。

其余发布检查见 [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)。

### 免责声明

本项目用于科研质量控制、可重复性、论文生产和交付支持，不提供临床诊断、治疗建议或监管认证，也不保证基金中标、论文接收或研究结论成立。

## English

LXQ is a Codex skill for biomedical, clinical, and bioinformatics research. It supports evidence-linked auditing, targeted corrections, reproducible analysis, manuscript development, and research deliverables. The current version is [`2.9.0`](VERSION).

### Latest update on the main branch

The [Biomedical Image Analysis Guide](lxq/references/biomedical-image-analysis-zh.md) loads on demand for fluorescence and confocal microscopy, histopathology, MRI/CT, and time-lapse imaging. It helps select segmentation, detection, or tracking baselines based on the image type, available annotations, and study endpoint. It also covers splitting data by participant, donor, or independent experimental sample and checking error in downstream counts, distances, and morphology measurements.

The [literature notes](lxq/references/biomedical-image-analysis-literature-zh.md) link to 55 unique papers and include detailed notes on 10. Both references are written in Chinese. See the [changelog](CHANGELOG.md) for version history and [PR #4](https://github.com/Jayen-Leung/LXQ-AI-Agent-Skill/pull/4) for the imaging update.

### Core capabilities

- Quality control for biomedical data and multi-omics workflows, including bulk RNA-seq, single-cell and spatial omics, WES/WGS, proteomics, metabolomics, and microbiome studies.
- Study design and statistical review for clinical and observational research.
- Evidence-driven manuscript production through the [SCI Manuscript Engine](lxq/references/sci-manuscript-engine.md), with study-type routing, an Evidence Map, a Scientific Story, and a Figure Storyboard.
- Evidence grading and claim-strength checks that bound causal and mechanistic conclusions by the available evidence.
- Manuscript, numerical consistency, scientific figure, and evidentiary image review, plus method selection and validation for quantitative biomedical imaging.
- Reviewer responses, submission packages, and data and code availability checks.
- Grant planning and review, including aims, methods, feasibility, risks, and budgets, plus Chinese and English research proposals for clients.
- Literature search, lawful full-text acquisition, close reading, and evidence synthesis. Chinese single-paper reports support Word and PDF delivery.
- Structured issue registers, evidence matrices, terminology ledgers, reproducibility checklists, and configurable `light`, `standard`, `strict`, and `forensic` review levels.
- Examples and regression scenarios, plus heuristic scoring for Chinese research proposals and grant drafts.

See the [Chinese capability and audit guide](lxq/references/lxq-functions-v2.5-zh.md) for the full inventory.

### Repository layout

```text
lxq-skill/
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── RELEASE_CHECKLIST.md
├── CHANGELOG.md
├── REGRESSION_REPORT.md
├── VERSION
├── .gitignore
├── .gitattributes
├── .github/workflows/validate.yml
├── tests/validate_repository.py
└── lxq/                         # Installable skill directory
    ├── SKILL.md
    ├── manifest.yaml
    ├── agents/
    ├── static/
    ├── references/
    │   ├── biomedical-image-analysis-zh.md
    │   ├── biomedical-image-analysis-literature-zh.md
    │   ├── sci-manuscript-engine.md
    │   └── manuscript-contracts/
    ├── bundled_skills/             # Bundled Nature specialist skills
    ├── bundled_catalogs/           # GPTomics and Orchestra AI Research catalogs
    └── scripts/
```

### Installation

Run the commands for your system from the repository root. To update an existing installation, back up the old `lxq` folder outside the skills directory before copying the new one.

**Windows PowerShell**

```powershell
$skillDir = Join-Path $HOME '.codex\skills'
$target = Join-Path $skillDir 'lxq'
if (Test-Path -LiteralPath $target) { throw 'Back up the existing LXQ folder outside the skills directory before installing.' }
New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
Copy-Item -LiteralPath '.\lxq' -Destination $target -Recurse
```

**macOS / Linux**

```bash
skill_dir="$HOME/.codex/skills"
if [ -e "$skill_dir/lxq" ] || [ -L "$skill_dir/lxq" ]; then
  printf '%s\n' 'Back up the existing LXQ folder outside the skills directory before installing.'
else
  mkdir -p "$skill_dir" && cp -R ./lxq "$skill_dir/lxq"
fi
```

Start a new Codex chat after installation or an update to load the latest skill metadata.

### Usage examples

```text
Use LXQ to audit this single-cell workflow and produce an issue register.

Use LXQ to analyze these confocal images. Compare nuclear segmentation methods,
hold out donors for validation, and report counting error.

Use LXQ to shortlist three projects based on this department's research
priorities and funding call, then prepare a client-facing proposal in English.

Use LXQ to find and lawfully obtain the relevant full texts, build an evidence
matrix, and review each paper.

Use LXQ to check whether sample counts and conclusions agree across the
manuscript, figures, supplements, and reviewer responses.

Use LXQ in strict mode to turn this project into a journal-ready manuscript.
```

Full-manuscript tasks follow this workflow.

```text
Fact Base
→ Study-Type Classification
→ Evidence Map
→ Evidence Strength Grading
→ Scientific Question Chain
→ Figure Storyboard
→ Results
→ Methods
→ Discussion
→ Introduction
→ Abstract
→ Title
→ Citation / Statistics / Figure-Text Consistency
→ Nature Reviewer / Polishing
→ LXQ Final QC
```

### Repository validation

The validator uses the Python standard library.

```bash
python tests/validate_repository.py
```

It checks skill metadata, routing paths, Python entry points, manuscript contracts, report templates, UTF-8 files, generated review bundles, evaluation cases, and scoring behavior. GitHub Actions runs the same validator on pushes and pull requests.

### Research integrity and safety

- Use LXQ for research quality control and reproducibility. Clinical diagnosis, treatment, and regulated decisions require qualified review.
- Keep patient-level data, protected health information, credentials, and unpublished research out of public issues, pull requests, tests, and examples.
- Report data, citations, ethics approvals, and results only when they can be verified. Obtain full texts through lawful, authorized access.
- Assess scientific validity separately from repository structure checks. Match causal and clinical claims to the design and evidence.

See [SECURITY.md](SECURITY.md) for details.

### Publishing a copy to GitHub

Initialize a repository in your local copy and update the remote URL to point to your GitHub repository.

```bash
git init
git add .
git commit -m "Release LXQ 2.9.0"
git branch -M main
git remote add origin https://github.com/<your-account>/<your-repository>.git
git push -u origin main
```

Review [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) and decide which license applies before redistributing your copy.

### Disclaimer

LXQ supports research quality control, reproducibility, manuscript development, and research delivery. Funding, editorial, regulatory, and scientific decisions remain with the relevant reviewers and authorities.
