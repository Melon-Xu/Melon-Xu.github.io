# 内容核对记录（不发布为网页）

核对日期：2026-09-18。此文档与 `local/` 原始资料均已排除 Jekyll 输出。

## 资料优先级和版本

1. 用户本次附件中的明确身份、毕业时间和求职意向。
2. 仓库根目录提供的 `MeilongXu_Resume.pdf`（两页，无明确版本日期）。其内容包含 May 2027 毕业、2026 Amazon 实习和 2026 论文，作为本次提供的最新简历采用；没有用文件修改时间判断版本。原 PDF 字节未修改，现作为明确的 CV 下载资源。
3. arXiv 最新版本、会议/出版社页面。
4. 旧仓库与本人主页；合作者主页仅作交叉核对和布局参考。

## 已落实的资料

| 内容 | 来源与处理 |
| --- | --- |
| 姓名 Meilong Xu / 徐梅隆 | 英文名、中文名来自原 `_config.yml`，保留正确写法 |
| final-year CS Ph.D. Candidate、May 2027 | 用户最新说明与 CV 毕业时间一致；删除旧 fourth-year 表述 |
| Chao Chen / Xiaoling Hu | 原主页合作关系、CV 导师记录；保留 Chao Chen 导师与 Xiaoling Hu 合作描述 |
| 邮箱 | 使用 CV 的 `meixu@cs.stonybrook.edu`，旧 Gmail 不再作为主要联系方式 |
| LinkedIn | 来自 CV PDF 中的实际超链接，不猜测账号 |
| Scholar / GitHub | CV、原 `_config.yml` 与公开 GitHub 账号匹配 |
| Amazon / Prime Video | CV：Applied Scientist Intern，May 2026–Present。只采用公开简历中工作方向的概述，不复制内部项目代号和业务指标 |
| TikTok / Data-TnS-Algo | CV：Research Scientist Intern，May–Sep 2025。沿用 CV 的 TikTok 命名，未擅自混用 Applied Scientist 职位 |
| Stony Brook GRA | CV：Sep 2022–Present，拓扑学习、diffusion、VLM post-training |
| 审稿 | 采用 CV 的 CVPR、NeurIPS、ICLR、ICML、ICCV、ECCV、ACL、EMNLP，以及 TPAMI、TMI、TNNLS；角色均为 Reviewer，不猜年份 |
| 奖项 | CV 中 NeurIPS 2025 Scholar Award、National Scholarship 2019–2020、First Class Scholarship 2018–2021；不添加未经核实的百分比 |

## 论文与状态来源

| 稳定 ID | 来源 | 核对结论 |
| --- | --- | --- |
| `topo-r1` | https://arxiv.org/abs/2603.13054 ，用户后续明确说明 | 2026 预印本；完整 9 位作者；贡献表述为通过 SFT 和带 topology-aware verifiable rewards 的 GRPO，使 VLM 具备 topology-aware perception capability；未写会议录用或在投信息 |
| `rb-ft` | https://arxiv.org/abs/2511.15923 | 2025 预印本；本人第一作者和完整 10 位作者；先 rationale 再 label 的两阶段微调 |
| `loc-path` | https://arxiv.org/abs/2512.05391 | 保留在完整列表，2025 预印本；使用最新摘要的 compress-before-fusion 概述 |
| `updiff-uda` | https://arxiv.org/abs/2509.22476 | 最新标题已改为 Multi-Channel Uncertainty-Weighted Score Matching for Conditional Diffusion in Medical UDA；页面明确 Accepted by ECCV 2026；替换旧 Bézier 预印本，不重复显示 |
| `rankbygene` | https://arxiv.org/abs/2411.15076 ，https://ieeexplore.ieee.org/document/11662129 | arXiv 明确 accepted by TMI 2026；出版社页面受验证限制，不填卷期页码/DOI；保留 Paper 和 arXiv |
| `diffusion-lpo` | CV，https://arxiv.org/abs/2510.01540 ，https://openreview.net/forum?id=ippWaS9PG9 ，https://openreview.net/pdf/ffaf5a65d1c1fbb39138127879e424007a9c1472.pdf | CV 与官方 PDF 的 ICLR 2026 声明一致，从原预印本迁移到 peer-reviewed；OpenReview forum 受访问验证限制 |
| `match` | https://arxiv.org/abs/2510.01532 ，https://openreview.net/forum?id=bTgxLGMGdF ，CV | NeurIPS 2025；作者顺序为 Meilong Xu、Xiaoling Hu、Shahira Abousamra、Chen Li、Chao Chen。原网页把中间两位顺序写反，已修复。共同一作由 CV 与论文第一页共同确认。未把 workshop Oral 标为主会 Oral |
| `topocellgen` | https://openaccess.thecvf.com/content/CVPR2025/html/Xu_TopoCellGen_Generating_Histopathology_Cell_Topology_with_a_Diffusion_Model_CVPR_2025_paper.html ，https://media.eventhosts.cc/Conferences/CVPR2025/CVPR_main_conf_2025.pdf | CVPR 2025 主会 Oral；主会议程中 Oral Session 5B 可核实 |
| `toposemiseg` | https://arxiv.org/abs/2311.16447 ，原仓库 | ECCV 2024；完整作者、代码、旧 poster/slides 路径均保留 |
| `topological-imaging` | CV，https://link.springer.com/chapter/10.1007/978-3-031-73967-5_12 | TGI3 @ MICCAI 2024 workshop；Springer 引用出版年是 2025，`venue_year: 2024` 用于会议分组，`citation_year: 2025` 用于 BibTeX。出版社将姓名写为 Meiliong Xu，本站按本人 CV 使用 Meilong Xu |
| `pstlfusion` | https://www.sciencedirect.com/science/article/abs/pii/S0031320322004101 ，原仓库、CV | Pattern Recognition 2022（官方索引为 Vol.132, Dec 2022）；作者和代码保留；直接 HTTP 请求 403，搜索索引可读取元数据 |
| `stdfusionnet` | https://ieeexplore.ieee.org/document/9416507 ，原仓库、作者代码库 | IEEE TIM 2021；保留原作者顺序及实际代码。出版社直接访问受验证限制 |

首页 8 篇：Topo-R1、RB-FT、UPDiff-UDA、RankByGene、Diffusion-LPO、MATCH、TopoCellGen、TopoSemiSeg。完整页 12 篇。各页由同一 YAML 渲染，不重复维护状态或作者。

arXiv BibTeX 按该版本源生成并明确标注“Citation for the arXiv version.”，不把未核实的出版信息补入引用。

## 图片来源

没有原仓库可复用的对应论文 teaser，故从原论文 PDF 提取完整 figure，只裁去周围正文/页边距，未生成或改写研究图。

| 图 | 原论文位置 |
| --- | --- |
| Topo-R1 | arXiv PDF 第 2 页 Figure 1 |
| RB-FT | 第 4 页 Figure 1 |
| UPDiff-UDA | 第 3 页 Figure 1 |
| RankByGene | 第 3 页 Figure 2 |
| Diffusion-LPO | 第 1 页 Figure 1 |
| MATCH | 第 5 页 Figure 3 |
| TopoCellGen | 第 4 页 Figure 2 |
| TopoSemiSeg | 第 5 页 Figure 3 |

8 张 WebP 共 473,576 bytes，统一容器使用 `object-fit: contain`，点击可查看大图。头像复用 `images/xml_avatar.png`，保持等比例自然裁切；原图片路径保留。

## 新闻日期

用户在 2026-09-18 的后续说明中明确确认：ECCV 结果公布于 Jun 2026、ICLR 结果公布于 Jan 2026、TMI 录用于 Aug 2026。三条新闻均使用录用语义；与 Topo-R1 的 Mar 2026 预印本新闻一起按月份倒序排列：Aug → Jun → Mar → Jan。Topo-R1 初次提交为 2026-03-13。旧新闻 Oct/Sep/Apr/Feb 2025 与 Jul 2024 来自原首页，未用执行日期或 arXiv 修订日期充当录用日期。

## 仍待确认、未擅自填写

- **AAAI 审稿**：附件背景提到，但最新 CV 服务列表没有该项，旧仓库也无独立记录。本次按最新 CV 保守未展示，需本人确认后再加。
- **实习经理/导师姓名**：CV 无记录，未添加；Amazon 结束月份未记录，沿用 CV 的 Present。
- **TMI 正式卷期页码/DOI**：未确认，保留 accepted 状态；录用月份已由本人确认并展示在新闻中。
- **个人 arXiv 作者页、OpenReview 个人页、ORCID、Hugging Face**：现有资料未提供可靠本人账号链接，不显示图标。单篇论文页未冒充作者页。
- **代码资源**：UPDiff-UDA 公共仓库仅有一份一行 README，尚无实现代码，已移除 Code 按钮。Topo-R1、RB-FT、LoC-Path、Diffusion-LPO 未找到已核实的公开实现入口，未添加。没有把公开 rebuttal 仓库当作项目入口。
- **CV 版本日期**：PDF 未标明确切更新日；未重制或虚构一个“更新于”日期。

## 链接访问限制

最终网页共有 30 个唯一外部 URL。24 个可访问，6 个不能完整验证正文：

- IEEE Xplore 两篇（11662129、9416507）：直接请求 HTTP 202，浏览工具显示需验证浏览器。
- OpenReview 两篇（bTgxLGMGdF、ippWaS9PG9）：HTTP 200 但为验证页。
- LinkedIn 本人链接：HTTP 999，账号 URL 来自 CV。
- ScienceDirect PSTLFusion：直接请求 HTTP 403，官方搜索索引可读。

以上不代表链接不存在。详细本地机器记录见 `local/external-link-check.json`。GitHub Code 链接还检查了仓库文件列表，展示的代码库均存在实际实现文件。
