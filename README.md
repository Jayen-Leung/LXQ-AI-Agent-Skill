# LXQ Research Quality Control Skill

LXQ 是面向医学、临床与生物信息学研究的 Codex Skill，提供证据关联的审核、修复、执行和交付流程。当前发布版本为 `2.5.0`。

## 主要能力

- 医学、生物信息学和多组学数据质量控制
- Bulk RNA-seq、单细胞、空间组学、WES/WGS、蛋白质组、代谢组和微生物组审核
- 临床/观察性研究设计与统计检查
- 论文、数字一致性、科学图表和证据图像审核
- 审稿回复、投稿包、数据与代码可用性
- 基金课题、研究目标、技术路线、风险和预算审核
- 中文/英文医学科研客户交付方案
- 文献检索、合法全文获取、精读和证据综合
- 结构化问题清单、证据矩阵、术语台账和复现清单
- `light`、`standard`、`strict`、`forensic` 四级调用强度
- 中文客户交付去AI味过滤、14段硬结构和预算—技术匹配
- 12个正反示例、30个eval三件套和任务输出契约
- 中文客户交付与基金方案启发式质量评分

完整中文功能说明见 [LXQ v2.5 全功能中文内部审核说明](lxq/references/lxq-functions-v2.5-zh.md)。

## 仓库结构

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
    └── scripts/
```

## 安装

将仓库中的 `lxq` 文件夹复制到 Codex Skills 目录。

Windows PowerShell：

```powershell
Copy-Item -LiteralPath ".\lxq" -Destination "$HOME\.codex\skills\lxq" -Recurse
```

macOS/Linux：

```bash
cp -R ./lxq "$HOME/.codex/skills/lxq"
```

若目标目录已经存在，请先备份旧版本，再有意识地更新；不要在不了解本地修改的情况下直接覆盖。安装或更新后，新开一个 Codex 对话以加载最新元数据。

## 使用示例

```text
调用 LXQ，审核这个单细胞分析流程并生成问题清单。

调用 LXQ，根据科室背景和基金指南筛选三个课题方向，生成客户可直接阅读的中文方案。

调用 LXQ，检索并合法获取相关文献，建立证据矩阵后逐篇精读。

调用 LXQ，检查论文、图表、补充材料和审稿回复中的样本量及结论是否一致。
```

## 本地验证

仓库测试只依赖 Python 标准库：

```bash
python tests/validate_repository.py
```

测试内容包括：

- Skill 基本结构和前置元数据
- 路由引用路径存在性
- 十个 Python 脚本语法和命令入口
- UTF-8 文件完整性
- `core`、`grant`、`literature` 和 `complete` 工作包生成与结构验证
- 中文基金客户交付模板和空文献清单验证
- 中文内部审核文件与 Skill 文件清单一致性
- 30个eval三件套、类别配额、rubric字段和评分权重
- 客户交付/基金质量评分器的正负向区分能力

GitHub Actions 会在推送和 Pull Request 时自动执行同一测试。

## 安全与科研边界

- LXQ 不是临床诊疗系统，不替代伦理、统计、遗传、病理、监管或编辑专家审核。
- 不要在公开 Issue、PR、测试或示例中提交患者级数据、受保护健康信息、访问凭据或未公开研究材料。
- 不得虚构数据、引用、伦理批准、数据库编号、前期结果或已经执行的分析。
- 文献全文仅能通过合法、授权的方式获取。
- 结构验证通过不等于科学有效性通过。

详见 [SECURITY.md](SECURITY.md)。

## 上传到 GitHub

在安装 Git 后，于本仓库目录执行：

```bash
git init
git add .
git commit -m "Release LXQ 2.5.0"
git branch -M main
git remote add origin https://github.com/<你的账号>/<仓库名>.git
git push -u origin main
```

也可以在 GitHub 网页创建空仓库后，将本目录内容整体上传。不要只上传压缩包作为仓库内容。

## 发布前必须决定

本仓库当前没有替你选择开源许可证。在公开发布前，请根据是否允许他人复制、修改和商业使用，选择合适的 `LICENSE`；未选择许可证时，默认版权规则通常不授予他人自由复用权。

其余发布检查见 [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md)。

## 免责声明

本项目用于科研质量控制、可重复性和交付支持，不提供临床诊断、治疗建议或监管认证，也不保证基金中标、论文接收或研究结论成立。
