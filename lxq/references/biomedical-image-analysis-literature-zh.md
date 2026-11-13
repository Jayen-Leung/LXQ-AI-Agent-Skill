# 生物医学图像分析文献学习笔记

2026-11-13

已浏览仓库 README 的任务分类和文献表。按英文 README 的医学应用表计，共 59 条记录，按题名去重后 55 篇，包含 2014–2019 年的论文与预印本。10 篇重点阅读的方法与实验见下文，其余条目的阅读深度在附录逐篇标明。计数范围为 README 的医学应用表。 [仓库 README](https://github.com/albarqouni/Deep-Learning-for-Medical-Applications#medical-applications)

## 重点论文

### 1. U-Net · 少量标注下的像素分割

- **方法。** 下采样路径提取上下文，上采样路径恢复分辨率，同尺度跳跃连接把细节送回解码器。原版用无填充卷积和重叠切块推理，并对粘连细胞之间的狭窄边界提高损失权重。Fig. 1–3 对应网络、切块和边界权重。 [原文](https://arxiv.org/pdf/1505.04597)
- **验证。** 原文在 EM 神经结构及相差、DIC 显微图像上评估。Table 2 的 PhC-U373 和 DIC-HeLa IoU 分别为 0.9203 和 0.7756。用在新显微数据时，若下游要计数，需另外检查实例合并、拆分和漏检。 [原文 Table 2](https://arxiv.org/pdf/1505.04597)

### 2. Suggestive Annotation · 优先标注不确定且有代表性的图像

- **方法。** 用多套 FCN 的预测分歧估计不确定性，用编码器特征衡量图像间相似性，再以集合覆盖选择下一批标注样本。原文与随机选择、只按不确定性选择进行了比较。 [原文 §2、Fig. 1](https://arxiv.org/pdf/1706.04737)
- **验证。** 在结直肠腺体和淋巴结超声分割上，作者报告以约 50% 的标注预算达到与当时参考方法相当或更优的表现。预算按揭示的标注像素计量。若要评估自己项目的标注效率，应另记录实际耗时。 [原文 §3、Fig. 5](https://arxiv.org/pdf/1706.04737)

### 3. AggNet · 多人标注有分歧时的有丝分裂检测

- **方法。** 用专家标注训练多尺度 CNN 生成乳腺 H&E 候选，再从多人投票中估计潜在标签及每位标注者的灵敏度、特异度，并更新检测器。原文在 AMIDA13 上比较了多种投票聚合方法。 [期刊原文](https://doi.org/10.1109/TMI.2016.2528120) · [作者论文全文，附录 C](https://mediatum.ub.tum.de/doc/1368117/47614.pdf)
- **可复用点。** 保留逐标注者标签和专家复核。候选式标注还要用全视野人工检查估计候选生成的漏检，因为标注者只能复核已经呈现的对象。 [作者论文全文，Fig. C.1](https://mediatum.ub.tum.de/doc/1368117/47614.pdf)

### 4. Xu 等 · 只有图像级标签时的 H&E 多实例学习

- **方法与验证。** 将一张结直肠组织病理图像作为一个包，图块作为实例，按“至少一个癌组织实例即可使整图为阳性”的假设训练。Table 3 中粗标签 MIL 与细标签监督的相对表现随特征方案而变。 [原文](https://dihana.cps.unizar.es/proceedings/ICASSP/2014/papers/p1645-xu.pdf)
- **可复用点。** 若只有切片级或患者级标签，可用 MIL 做分类。若还要定位、计数或量面积，应拿单独的人工局部标注检验这些输出。 [原文 §3–4](https://dihana.cps.unizar.es/proceedings/ICASSP/2014/papers/p1645-xu.pdf)

### 5. Payan 与 Montana · 用 3D CNN 分类 ADNI 结构 MRI

- **方法与验证。** 用 3D 图块预训练稀疏自编码器，为卷积层提供初始滤波器，在 ADNI 上比较 2D 与 3D CNN。原文报告 2,265 次扫描，三分类准确率分别为 85.53% 和 89.47%，AD 对健康对照的准确率均为 95.39%。这些数值来自该论文的内部划分。 [原文 §2、Table 2](https://arxiv.org/pdf/1502.02506)
- **可复用点。** 2D 与 3D 应在同一受试者级划分中比较。对有重复访视的数据，所有扫描和派生图块都跟随同一受试者进入同一数据分区。已有独立实验证明脑 MRI 按切片拆分会抬高测试表现。 [MRI 泄漏对照实验](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604922/)

### 6. Hosseini-Asl 等 · 结构 MRI 的跨数据集预训练

- **方法与验证。** 在 CADDementia 的结构 MRI 上训练 3D 卷积自编码器，将编码层迁移到 ADNI 分类网络。原文报告源数据 30 名受试者、目标数据 210 名受试者，ADNI 内部用十折交叉验证评估五项二分类或三分类任务。 [原文 §2–3](https://arxiv.org/pdf/1607.00556)
- **可复用点。** 预训练来源、目标域微调用样本和最终测试样本需分别记录。该论文的结果对应目标域内交叉验证。 [原文 §3](https://arxiv.org/pdf/1607.00556)

### 7. Parisot 等 · 影像与非影像信息联合预测 MCI 转归

- **方法与验证。** 用影像特征表示节点，用表型相似性定义边，再用半监督图卷积。ADNI 分析含 540 名 MCI 受试者和 1,675 个样本，使用解剖区域体积与年龄、性别信息。论文明确把同一受试者的重复访视放在同一折。 [原文 §2.2、§3](https://arxiv.org/pdf/1703.03020)
- **可复用点。** 若目标是预测将来转归，要预先固定预测时点、可用访视窗口和结局窗口。部署需要预测新受试者时，应检验模型在新增节点或独立队列上的表现，并用同一划分比较影像模型与影像加表型模型。 [原文 §2–3](https://arxiv.org/pdf/1703.03020)

### 8. Christ 等 · 先分器官，再分小病灶

- **方法与验证。** 第一个 FCN 分割肝脏，第二个 FCN 在肝脏区域内分割病灶，并用 3D CRF 细化结果。原文评估了腹部 CT 上的肝脏与病灶分割。 [原文](https://arxiv.org/pdf/1610.02177)
- **可复用点。** 类似的级联可以先勾画组织、细胞或胞体范围，再在范围内检测小目标。验证时用自动生成的上游掩膜跑完整流程，检查上游漏分是否把真实小目标排除在外。 [原文](https://arxiv.org/pdf/1610.02177)

### 9. Kamnitsas 等 · 跨扫描协议的脑病灶分割

- **方法与验证。** 分割网络使用源域标签训练，同时对抗域判别器，使特征较难区分来源。实验用两个创伤性脑损伤 MRI 数据库，使用目标域半数受试者的无标签数据做适配，另半数测试，再交换两折。 [原文 §3、Fig. 3](https://arxiv.org/pdf/1612.08894)
- **可复用点。** 当显微镜、染色或扫描中心发生变化时，分开评估直接迁移和使用新域数据后的性能，并按批次、中心或仪器报告表现。论文的实验对应可取得目标域无标签数据的场景。 [原文 §3–4](https://arxiv.org/pdf/1612.08894)

### 10. 血涂片显微图像的条件 GAN 增强

- **方法与验证。** 仓库中的 *Red blood cell image generation for data augmentation using Conditional Generative Adversarial Networks* 从掩膜生成血涂片图像，并对真实数据与合成数据混合训练后的分割、目标检测进行实验。 [原文](https://arxiv.org/pdf/1901.06219)
- **可复用点。** 合成图像若用于增强，应和同一训练预算下的常规增强比较，最终用真实且独立留出的样本评价。尤其检查稀有形态和小目标是否被生成器过度简化。 [原文](https://arxiv.org/pdf/1901.06219)

## 方法应用与验证

| 图像与目标 | 可比较的方法 | 需要验证的输出 |
| --- | --- | --- |
| 荧光或共聚焦显微图像中的细胞体、细胞核 | 传统阈值与分水岭作为简单基线，Cellpose 或 StarDist 作为实例分割候选。 | 按细胞匹配计算检出率和精确率，检查粘连、拆分、漏检，以及每视野计数误差。 [Cellpose](https://www.nature.com/articles/s41592-020-01018-x) · [StarDist](https://arxiv.org/abs/1806.03535) |
| VDAC1 或其他线粒体标记的空间分布与形态 | 先界定细胞、胞体或核边界，再分割线粒体标记信号。若原始数据足以解析细管与分支，可将 MiNA 或 MitoGraph 的网络指标纳入比较。 | 原始图像叠加掩膜，核对轴向间距、像素大小、视野归属。分别验证标记信号的面积或体积分数、到核边界的距离，及在可解析时的骨架长度和连通性。 [MiNA](https://pubmed.ncbi.nlm.nih.gov/28314612/) · [MitoGraph](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322684/) |
| H&E / IHC 切片中的细胞计数或病理表型 | 核实例任务可比较 HoVer-Net、StarDist。只有切片级或患者级标签时可评估 MIL。 | 对局部计数或分割保留独立人工标注。若做病例分类，按患者分组后再切图块。 [HoVer-Net](https://arxiv.org/abs/1812.06499) · [MIL 原文](https://dihana.cps.unizar.es/proceedings/ICASSP/2014/papers/p1645-xu.pdf) |
| MRI、CT 或三维体数据的结构分割 | 可从 3D U-Net 或 nnU-Net 建立基线，并按体素间距和任务对比 2D 与 3D。 | 器官可报告 Dice 和边界距离。病灶稀少时加报病灶级灵敏度及每病例假阳性数。 [3D U-Net](https://arxiv.org/abs/1606.06650) · [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) · [Metrics Reloaded](https://www.nature.com/articles/s41592-023-02151-z) |

- 对于线粒体定位研究，固定图可以给出静态标记信号的分布和可解析的形态。运输速度、停留时间或分裂融合事件需要时间序列与追踪。VDAC1 信号强度的变化应按该标记及成像条件解释。 [Mitometer](https://www.nature.com/articles/s41592-021-01234-z)
- 显微组间统计依据实验设计，以供体、动物或独立培养重复为单位。保留视野和细胞的层级信息，用样本汇总或分层模型估计组间效应。模型验证按原始生物样本划分，图块、相邻切片和重复拍摄随同源样本进入同一分区。最终除分割分数外，也校验模型输出的数量、距离或形态指标与人工参考值之间的偏差。 [Metrics Reloaded](https://www.nature.com/articles/s41592-023-02151-z) · [影像切分对照实验](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604922/)

## 仓库论文索引

按在 README 中首次出现的主要任务列出。初筛以摘要或原文可获取内容为主。两项题录与方法主题条目仍需核对具体实验。显微和体数据的补充文献已在上表给出。

### 标注与弱监督

- 结直肠 H&E 的多实例学习 · 重点阅读 · [来源](https://dihana.cps.unizar.es/proceedings/ICASSP/2014/papers/p1645-xu.pdf)
- AggNet 多人标注与有丝分裂检测 · 重点阅读 · [来源](https://doi.org/10.1109/TMI.2016.2528120)
- Suggestive Annotation 主动学习 · 重点阅读 · [来源](https://arxiv.org/abs/1706.04737)

### 分类与预测

- 多尺度 CT 肺结节分类 · 初筛 · [来源](https://link.springer.com/chapter/10.1007/978-3-319-19992-4_46)
- Payan 与 Montana 的 ADNI 3D CNN · 重点阅读 · [来源](https://arxiv.org/abs/1502.02506)
- 白内障核混浊分级 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/26080373/)
- 膝关节 X 线骨关节炎分级 · 初筛 · [来源](https://arxiv.org/pdf/1609.02469)
- 甲状腺细胞病理移动应用 · 题录与方法主题 · [来源](https://doi.org/10.1117/12.2216468)
- 跨数据集预训练的 DSA-3D-CNN · 重点阅读 · [来源](https://arxiv.org/abs/1607.00556)
- 多分辨率皮肤病变分类 · 初筛 · [来源](https://www.cs.sfu.ca/~hamarneh/ecopy/miccai_mlmi2016a.pdf)
- 黑色素瘤筛查的迁移学习 · 初筛 · [来源](https://arxiv.org/pdf/1609.01228.pdf)
- CT 肺结节多视角假阳性过滤 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/26955024/)
- DeepLung 3D 肺结节检测与分类 · 初筛 · [来源](https://arxiv.org/abs/1801.09555)
- 多模态脑肿瘤 MRI 生存时间预测 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/28149967/)
- 超声乳腺病灶和 CT 肺结节分类 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/27079888/)
- 无监督乳腺密度分割和风险评分 · 初筛 · [来源](https://ieeexplore.ieee.org/document/7412749/)
- 整张乳腺 X 线图像的多实例分类 · 初筛 · [来源](https://link.springer.com/chapter/10.1007/978-3-319-66179-7_69)
- 人群图卷积与 MCI 转归 · 重点阅读 · [来源](https://arxiv.org/abs/1703.03020)
- 皮肤肿瘤图像分类 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/28117445/)
- SurvivalNet 肝肿瘤分割与生存预测 · 初筛 · [来源](https://arxiv.org/abs/1702.05941)

### 检测与定位

- 3D 体积图像解剖标志点检测 · 初筛 · [来源](https://comaniciu.net/Papers/3D_DeepLearningLandmark_MICCAI15.pdf)
- 迁移学习定位胎儿超声标准切面 · 初筛 · [来源](https://researchportal.hkust.edu.hk/en/publications/standard-plane-localization-in-fetal-ultrasound-via-domain-transf/)
- MRI 股骨远端标志点检测 · 初筛 · [来源](https://www.researchwithrutgers.org/en/publications/automated-anatomical-landmark-detection-ondistal-femur-surface-us/)
- 迁移学习与 RNN 检测胎儿超声标准切面 · 初筛 · [来源](https://link.springer.com/chapter/10.1007/978-3-319-24553-9_62)
- 热图回归定位多个解剖标志点 · 初筛 · [来源](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_bischof/mib/paper_pdfs/MICCAI2016_CNNHeatmaps.pdf)
- 基于智能体的解剖标志点定位 · 初筛 · [来源](https://www5.informatik.uni-erlangen.de/fileadmin/research/Publikationen/2016/Ghesu16-AAA.pdf)
- 全卷积网络实时检测胎儿超声标准切面 · 初筛 · [来源](https://www.doc.ic.ac.uk/~bkainz/publications/Kainz_MICCAI2016b.pdf)
- 时序回归识别心脏舒张末期与收缩末期 · 题录与方法主题 · [来源](https://link.springer.com/chapter/10.1007/978-3-319-46726-9_31)
- 候选检测与随机多视角聚合 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/26441412/)
- PET/CT 肺结节检测及假阳性过滤 · 初筛 · [来源](https://aapm.onlinelibrary.wiley.com/doi/10.1118/1.4948498)
- 3D CNN 脑微出血检测 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/26886975/)
- 弱监督病灶定位的 Self-Transfer Learning · 初筛 · [来源](https://link.springer.com/chapter/10.1007/978-3-319-46723-8_28)
- 眼底出血检测的选择性采样 · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/26886969/)
- AnoGAN 无监督异常检测 · 初筛 · [来源](https://arxiv.org/abs/1703.05921)
- CathNets 导管电极检测及单视角深度估计 · 初筛 · [来源](https://campar.cs.tum.edu/pub/baur2016miar/baur2016miar.poster.pdf)
- DeepEM 弱监督肺结节检测 · 初筛 · [来源](https://arxiv.org/abs/1805.05373)

### 分割

- U-Net 生物医学图像分割 · 重点阅读 · [来源](https://arxiv.org/abs/1505.04597)
- DeepMedic 多尺度 3D 脑病灶分割 · 初筛 · [来源](https://arxiv.org/abs/1603.05959)
- AnatomyNet 头颈 CT 全体积分割 · 初筛 · [来源](https://arxiv.org/abs/1808.05238)
- CT 肝脏与病灶级联分割 · 重点阅读 · [来源](https://arxiv.org/abs/1610.02177)
- 3D CNN 与形状模型分割 MRI 椎体 · 初筛 · [来源](https://doi.org/10.1007/978-3-319-46723-8_50)
- CT/MRI 肝脏与肿瘤的级联分割 · 初筛 · [来源](https://arxiv.org/abs/1702.05970)
- q-Space 深度学习扩散 MRI · 初筛 · [来源](https://pubmed.ncbi.nlm.nih.gov/27071165/)
- 对抗训练和结构预测分割乳腺肿块 · 初筛 · [来源](https://arxiv.org/abs/1710.09288)
- 3D 深度监督的 CT 肝脏分割 · 初筛 · [来源](https://arxiv.org/abs/1607.00582)
- 脑病灶分割的无监督域适应 · 重点阅读 · [来源](https://arxiv.org/abs/1612.08894)
- FCN 结构化预测分割眼底血管 · 初筛 · [来源](https://arxiv.org/pdf/1611.02064)

### 配准

- 基于智能体的 3D 图像配准 · 初筛 · [来源](https://arxiv.org/abs/1611.10336)

### 重建

- 动态 MRI 的级联 CNN 重建 · 初筛 · [来源](https://arxiv.org/abs/1704.02422)
- 压缩感知 MRI 的 GAN 重建 · 初筛 · [来源](https://www.doc.ic.ac.uk/~bglocker/public/mednips2017/med-nips_2017_paper_7.pdf)

### 合成增强

- 血涂片显微图像的条件 GAN 增强 · 重点阅读 · [来源](https://arxiv.org/abs/1901.06219)
- 粗到细 GAN 增强脑肿瘤分割 · 初筛 · [来源](https://arxiv.org/pdf/1805.11291.pdf)
- 合成脑肿瘤 MRI 用于增强和匿名化研究 · 初筛 · [来源](https://arxiv.org/pdf/1807.10225.pdf)
- GAN 增强医学影像训练数据 · 初筛 · [来源](https://arxiv.org/pdf/1810.10863.pdf)
- GAN 增强 CT 肝病灶分类 · 初筛 · [来源](https://arxiv.org/pdf/1803.01229.pdf)
