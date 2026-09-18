# 内容维护

访客内容使用英文。所有业务内容都由 YAML 提供；不需要安装 Node 或打包 JavaScript。

| 修改内容 | 编辑位置 |
| --- | --- |
| 简介、身份、毕业时间、求职提示、邮箱 | `_data/profile.yml` |
| 增加或更新经历 | `_data/experience.yml`，按最新经历优先排列 |
| 研究方向及代表作 | `_data/research.yml`，`papers` 引用论文稳定 ID |
| 增加论文、作者、链接、状态、精选 | `_data/publications.yml` |
| 添加新闻 | `_data/news.yml`，最新条目放前面，默认显示前 6 条 |
| 修改审稿记录 | `_data/service.yml` |
| 教育、奖项 | `_data/profile.yml` 的 `education`、`awards` |
| 替换 CV | 用新本人 PDF 覆盖根目录 `MeilongXu_Resume.pdf`，保持路径不变 |
| 修改图标链接 | `_data/profile.yml` 的 `socials`；新图标类型在 `_includes/light-icon.html` 增加 |
| 调整排版 | `assets/site.css`；页面骨架 `_layouts/minimal-light.html` |
| 站点标题、description、生产域名 | `_config.yml` |

## 论文例子

下面是现有条目的结构示例；更新现有论文时编辑其条目，不重复追加同一论文。

```yaml
- id: topo-r1
  short_title: Topo-R1
  title: 'Topo-R1: Detecting Topological Anomalies via Vision-Language Models'
  authors:
    - Meilong Xu
    - Qingqiao Hu
    - Xiaoling Hu
    - Shahira Abousamra
    - Xin Yu
    - Weimin Lyu
    - Kehan Qi
    - Dimitris Samaras
    - Chao Chen
  venue: arXiv preprint
  venue_year: 2026
  status: preprint
  selected: true
  summary: Equips vision-language models with topology-aware perception capabilities through supervised fine-tuning (SFT) and GRPO with topology-aware verifiable rewards.
  arxiv_id: '2603.13054'
  arxiv_year: 2026
  teaser: /assets/teasers/topo-r1.webp
  teaser_alt: Topo-R1 framework figure from the paper
  links:
    arXiv: https://arxiv.org/abs/2603.13054
```

`status` 支持 `preprint`、`accepted`、`published`。录用时同时更新 `venue`、`venue_year` 和 `status`，保留 arXiv 链接；正式出版后改为 `published`。`venue_year` 是会议/期刊分组年份，不是 arXiv 初次上传年。`arxiv_year` 只用于明确标注的 arXiv BibTeX。无 arXiv 的论文默认生成基本出版引用；若正式引用年份与会议年份不同，使用 `citation_year`（现有 TGI3 条目即如此）。

`selected: true` 控制首页精选，完整页自动显示全部条目。增删精选后如有意改变 8/12 篇数量，同步更新 `scripts/check_site.py` 的数量断言。论文稳定 `id` 不随标题修改而更改，避免破坏已分享的锚点。

`links` 的键直接成为按钮文字：Paper、arXiv、Code、Project、Slides、Poster 等。不存在就删除该键，不留空 URL、平台首页或 `#`。只有实际发布实现代码才用 Code。BibTeX 自动由同一条数据生成，无须维护第二份作者信息。

可选 `distinction: Oral`；只有来源明确时填写。共同一作在 `equal_contribution` 中按姓名列出；作者原始数组始终保持完整顺序。无图时省略 `teaser` 和 `teaser_alt`，模板自动排为纯文字。

## 经历与新闻例子

```yaml
# _data/experience.yml
- organization: Amazon
  team: Prime Video
  role: Applied Scientist Intern
  date: May 2026 – Present
  summary: Physics-grounded video generation with simulation-based planning and verification.
```

结束实习后更新 date；未核实的经理姓名、月份或内部指标不添加。桌面和手机共用这一份经历数据。

```yaml
# _data/news.yml
- date: 'Jun 2026'
  text: 'UPDiff-UDA accepted at <strong>ECCV 2026</strong>.'
  paper: updiff-uda
```

只有月份得到确认才写 `Mar 2026` 等；日期字段加引号。`paper` 可省略，填写时必须对应论文 ID。Show more 使用原生 details，禁用 JavaScript 仍可操作。

审稿记录直接改 `conferences`、`journals` 数组。没有明确年份就只写 venue；不要从论文 venue 推导审稿经历。奖项数组为空时不会输出空板块。

## 修改后验证

```sh
./scripts/site build
python3 scripts/check_site.py
./scripts/site serve
```

打开 <http://127.0.0.1:4000/> 与 `/publications/`，检查手机宽度、图片、标题、链接和 BibTeX。更新 YAML/HTML/CSS 时预览自动重建，浏览器需刷新；更新 `_config.yml` 后要重启预览。

`_site/` 是生产输出；`local/preview/` 是预览输出。两者都不要提交。`docs/`、`scripts/`、`licenses/`、原始论文、截图、依赖与本地备份都不进入网站；附件 prompt 保持在仓库外。仅根目录的本人简历 PDF 被明确用于公开下载。

旧 `_pages/`、`_posts/`、`_publications/` 等是停用的 Academic Pages 示例/历史资料，新站点不加载旧主题 CSS/JS。不要通过修改旧页面更新内容。
