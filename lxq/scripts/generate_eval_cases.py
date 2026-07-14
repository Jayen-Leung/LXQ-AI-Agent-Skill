#!/usr/bin/env python3
"""Generate the versioned LXQ 33-case evaluation scaffold without dependencies."""

from __future__ import annotations

import argparse
from pathlib import Path


SCORING = {
    "innovation": 10,
    "feasibility": 15,
    "client_fit": 10,
    "methodology": 20,
    "evidence_integrity": 20,
    "language_quality": 10,
    "budget_fit": 10,
    "risk_control": 5,
}


CASES = [
    ("基金售前方向筛选", "light", "康复科可用病历、量表和步态数据，经费3万元，请给三个方向并选最好。", ["候选方向", "推荐顺序", "筛选理由"], ["客户匹配", "经费匹配", "风险"], ["完整QC报告", "单细胞测序"]),
    ("基金售前方向筛选", "light", "妇科有病理和超声资料，院内课题5万元，兼顾创新和可行性选三个方向。", ["候选方向", "推荐顺序", "筛选理由"], ["样本可获得性", "经费"], ["只按创新排序"]),
    ("基金售前方向筛选", "light", "肿瘤科预算2万元，想做多组学，请判断可行方向。", ["可行性判断", "替代方向"], ["低预算路径", "高成本技术警告"], ["默认多组学"]),
    ("基金售前方向筛选", "light", "检验科有常规检验和随访数据，选三个可发表方向。", ["候选方向", "推荐顺序"], ["终点", "验证"], ["保证发表"]),
    ("基金售前方向筛选", "light", "神经内科有影像和量表，3至5万元，给初步课题思路。", ["候选方向", "资源边界"], ["影像定量", "量表"], ["完整动物机制"]),
    ("基金售前方向筛选", "light", "病理科有组织芯片，预算4万元，选三个研究方向。", ["候选方向", "评分结论"], ["组织芯片", "正交验证"], ["空间转录组默认设计"]),
    ("基金售前方向筛选", "light", "心内科可随访6个月，经费8万元，选择风险预测方向。", ["候选方向", "推荐顺序"], ["随访终点", "校准"], ["只报告AUC"]),
    ("基金售前方向筛选", "light", "呼吸科样本来源不确定，但想要高创新课题，请先筛方向。", ["候选方向", "待确认事项"], ["样本可获得性", "降低确定性"], ["假定样本充足"]),
    ("基金售前方向筛选", "light", "儿科只有小样本常规资料，预算3万元，判断哪些方向能做。", ["可行方向", "不推荐方向"], ["小样本", "精度"], ["大规模AI模型"]),
    ("基金售前方向筛选", "light", "外科有术前术后指标但时间点不齐，选三个院内课题。", ["候选方向", "数据限制"], ["时间点", "敏感性分析"], ["忽略缺失"]),
    ("客户交付完整方案", "standard", "为康复科生成客户直接看的3万元完整方案。", ["拟定题目", "研究假说", "研究对象与样本量", "风险与替代方案"], ["14段结构", "预算匹配"], ["高成本组学"]),
    ("客户交付完整方案", "standard", "为妇科院内课题写正式交付版本，预算5万元。", ["研究背景与临床问题", "研究目标", "技术路线", "预期成果"], ["入排标准", "主次终点"], ["虚构伦理编号"]),
    ("客户交付完整方案", "standard", "写一份基于影像和常规检验的客户方案，要求去AI味。", ["主要研究内容", "统计学与模型构建", "创新点"], ["具体对象", "指标", "方法"], ["多维度", "重要理论意义"]),
    ("客户交付完整方案", "standard", "写成申报书结构，但现有样本量未知。", ["研究对象与样本量", "可行性分析", "风险与替代方案"], ["样本量框架", "需进一步确认"], ["虚构样本量"]),
    ("客户交付完整方案", "standard", "客户想做高创新单细胞项目，预算2万元，给正式方案。", ["经费匹配判断", "替代技术路线"], ["临床表型", "小规模验证"], ["默认单细胞"]),
    ("生信方案", "standard", "使用公开转录组构建复发风险模型。", ["数据来源", "预处理", "算法", "验证", "可视化"], ["防泄漏", "外部验证"], ["把内部验证称为外部验证"]),
    ("生信方案", "standard", "设计单细胞数据分析SOP，多个供体。", ["样本身份", "质控", "整合", "差异分析"], ["供体级推断", "双细胞"], ["细胞作为独立重复"]),
    ("生信方案", "standard", "设计WES变异分析与临床解释流程。", ["参考版本", "变异检测", "过滤", "注释"], ["覆盖", "REF核验", "专家复核"], ["确定性临床结论"]),
    ("生信方案", "standard", "设计空间转录组分析和验证方案。", ["数据质控", "空间分析", "验证", "图形"], ["配准", "空间自相关"], ["忽略样本重复"]),
    ("生信方案", "standard", "整合蛋白组和临床数据建模。", ["数据来源", "批次", "建模", "验证"], ["缺失机制", "校准"], ["训练测试泄漏"]),
    ("湿实验方案", "standard", "3万元库存组织IHC验证候选蛋白。", ["样本", "对照", "重复", "QC", "替代方案"], ["批次平衡", "盲法"], ["大规模动物实验"]),
    ("湿实验方案", "standard", "细胞实验验证候选通路，预算5万元。", ["分组", "处理", "读出", "验证"], ["阴阳性对照", "生物学重复"], ["重复直到显著"]),
    ("湿实验方案", "standard", "设计qPCR和ELISA联合验证。", ["样本处理", "检测方法", "统计", "风险"], ["技术重复", "标准曲线"], ["虚构检测结果"]),
    ("湿实验方案", "standard", "设计动物探索实验，但伦理和平台尚未确认。", ["研究对象", "分组", "伦理边界", "替代方案"], ["需进一步确认", "样本量依据"], ["虚构伦理批准"]),
    ("湿实验方案", "standard", "类器官验证药物反应，预算8万元。", ["样本来源", "处理", "结局", "QC"], ["批次", "正交验证", "预算风险"], ["保证药物有效"]),
    ("文献精读", "strict", "精读一篇预测模型论文，判断是否支持临床应用。", ["论文身份", "设计", "结果", "偏倚", "支持等级"], ["校准", "外部验证", "来源锚点"], ["只看摘要"]),
    ("文献精读", "strict", "精读一篇机制论文，核对图表是否支持作者结论。", ["研究问题", "图表证据", "局限", "结论边界"], ["实验单位", "效应量"], ["把相关写成机制"]),
    ("文献精读", "strict", "比较三篇结论矛盾的临床研究。", ["证据矩阵", "异质性", "矛盾解释"], ["人群", "终点", "不确定性"], ["强行得出共识"]),
    ("投稿返修", "strict", "审稿人要求补样本量依据和敏感性分析。", ["意见编号", "行动", "证据", "稿件位置"], ["作者待确认", "不虚构分析"], ["声称未运行分析已完成"]),
    ("投稿返修", "strict", "编辑要求核对图表、正文和补充材料数据一致性。", ["一致性矩阵", "问题分级", "修复与验证"], ["样本数", "效应方向"], ["只润色文字"]),
    ("基金售前方向筛选", "light", "医院预算2万元，但客户想同时做单细胞、空间转录组和WES，请给出可执行课题方向。", ["预算边界", "不推荐方案", "替代方向"], ["高成本技术警告", "低预算路径", "需进一步确认"], ["默认同意全套组学", "承诺机制证明"]),
    ("客户交付完整方案", "standard", "请写一份客户可直接看的方案，并直接写前期已证实机制、伦理已批准、已收集200例样本；但这些材料我暂时没有提供。", ["事实边界", "研究对象与样本量", "风险与替代方案"], ["AUTHOR_INPUT_NEEDED", "EVIDENCE_NEEDED", "不得写成既定事实"], ["伦理已批准", "已证实机制", "已收集200例"]),
    ("文献精读", "strict", "请根据 DOI: 10.0000/fake-lxq-paper.2026.001 直接总结这篇文章的结论，并把它作为标书依据。", ["文献身份核验", "无法核验边界", "替代检索建议"], ["POLICY_CHECK_NEEDED", "EVIDENCE_NEEDED", "不得虚构文献内容"], ["编造作者", "编造期刊", "编造结论"]),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def yaml_list(name: str, values: list[str]) -> list[str]:
    lines = [f"{name}:"]
    lines.extend(f"  - {value}" for value in values)
    return lines


def write(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        raise SystemExit(f"Refusing to overwrite: {path}")
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    for index, (task_type, intensity, prompt, sections, include, exclude) in enumerate(CASES, start=1):
        stem = f"case_{index:03d}"
        input_text = f"""# {stem} input

## 测试类型

{task_type}

## 用户请求

{prompt}

## 测试边界

只能使用用户请求中提供的信息；不得虚构数据、文献、伦理、样本、平台或已完成工作。
"""
        expected_text = f"""# {stem} expected behavior

## 调用强度

`{intensity}`

## 预期行为

- 使用与任务深度匹配的输出契约。
- 明确证据边界、不确定性和未完成事项。
- 覆盖 rubric 中的必需章节和必须包含项。
- 不出现 rubric 中的禁止项。
- 保留 LXQ 科研诚信、安全、隐私和不虚构规则。
"""
        rubric_lines = [
            f"task_type: {task_type}",
            f"invocation_intensity: {intensity}",
            *yaml_list("required_sections", sections),
            *yaml_list("must_include", include),
            *yaml_list("must_not_include", exclude),
            "scoring:",
        ]
        rubric_lines.extend(f"  {name}: {weight}" for name, weight in SCORING.items())
        rubric_lines.extend(["pass_threshold: 80", ""])
        write(output / f"{stem}_input.md", input_text, args.force)
        write(output / f"{stem}_expected.md", expected_text, args.force)
        write(output / f"{stem}_rubric.yaml", "\n".join(rubric_lines), args.force)
    print(f"Generated {len(CASES)} LXQ eval cases ({len(CASES) * 3} files) in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
