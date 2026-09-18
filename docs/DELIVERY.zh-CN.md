# 本地交付与发布说明

## Git 与迁移范围

- 起始分支 `master`，起始提交 `87d6fdd713f61b878d5ee3aca8e7dd2a6af2a412`。
- 当前独立分支 `codex/minimal-light-refactor`。
- 原 remote：`https://github.com/Melon-Xu/Melon-Xu.github.io.git`，未修改。
- 初始已跟踪文件无未提交改动；原有未跟踪 `.DS_Store` 与 `MeilongXu_Resume.pdf` 均保留。`.DS_Store` 已忽略；简历作为本次指定公开 CV 资源纳入版本管理。
- 首次本地交付未 commit 或 push。用户于 2026-09-18 后续授权将所有修改及最新 CV 提交并推送到远端重构分支；不合并到 `master`，不发布网站或改动 GitHub 设置。
- 当前生产 URL 为 `https://melon-xu.github.io`，`baseurl: ""`，没有 CNAME，也未复制主题示例域名。

首页、`/publications/`、`/cv/` 迁移到本地 Minimal Light 适配。`/about/`、`/about.html`、`/resume`、`/resume/` 保留静态兼容跳转；新增 `/publications.html` 和 `/cv.html` 兼容入口。它们是 HTML 跳转，不是服务器 301。全部原 `files/`、图片路径和 TopoSemiSeg PDF/slides/poster 资源保留。

旧博客、teaching、portfolio、talks、示例 publication 独立页及模板 CV 内容均属于 Academic Pages 示例，不再输出。原源码仍在仓库、原 Git 提交中可恢复。旧主题的 CSS、JS 不加载；新主题没有远程依赖或 analytics。

## 本地预览与检查

```sh
cd /Users/meilongx/Desktop/Melon-Xu.github.io
./scripts/site build
python3 scripts/check_site.py
./scripts/site serve
```

打开 <http://127.0.0.1:4000/>。停止前台服务：Ctrl+C。本次交付时预览服务保持运行。

当前机器使用 `local/ruby/portable-ruby/3.4.5/` 中的隔离 Ruby 和 `vendor/bundle/` 依赖，不更改系统 Ruby。脚本自动选择本地运行时；另一台电脑安装 Ruby 3.2+、Bundler 2.6.9 后，先执行 `./scripts/site install`。`Gemfile.lock` 纳入版本管理。

生产输出在 `_site/`；预览输出在 `local/preview/`。即使本地预览，canonical/分享元数据仍用正式域名。旧别名静态跳转由 Jekyll 插件生成，目标是正式原网址；浏览本地新版请使用根路径、`/publications/` 或 `/cv/`。

已执行：

- Jekyll **生产构建成功**，无 Liquid/YAML/Sass 错误；纯 CSS 页面不使用旧 Sass 构建管线。
- 静态检查：10 个 HTML 输出、123 个站内链接/资源引用、首页 8 篇/完整页 12 篇；0 个错误。原文件目录逐一比对、CV 原始字节一致。随后通过本地 HTTP 实际请求首页、完整论文、CV、兼容路径和全部 8 个旧 PDF，均返回 200，PDF 内容一致。
- 桌面 1440×1000、笔记本 1024×900、手机 390×844 实际浏览器渲染检查。
- 手机无横向溢出、无破图，首页顺序为个人信息 → 导航 → 简介/求职 → 经历 → 研究等内容。完整论文页手机端优先显示论文。
- 高侧栏使用正常滚动，仅当完整高度能容纳于视口时启用 sticky。
- 已检查原生 Show more/BibTeX 的键盘 Enter 操作、可见焦点、锚点、社交图标、CV 和 mailto。
- 生产 canonical/sitemap 为原域名；内部 docs、scripts、依赖、原始资料、截图与备份不在发布输出中。
- 外部 URL 24/30 可访问；6 个访问限制详见内容核对记录。没有把返回验证码的 HTTP 200 当作内容验证成功。

截图保存在 `local/screenshots/`（不提交、不公开）：`desktop-1440.png`、`laptop-1024.png`、`mobile-390.png`、`desktop-publications.png`、`mobile-publications.png`、`mobile-experience.png`。

## 保留原网址的提交与后续上线步骤

公开 GitHub API 显示仓库使用 `pages-build-deployment` 动态 Pages 工作流，最近可见部署来自 `master` 的 `github-pages` 环境。仓库本身没有自定义 Actions workflow。本次沿用这个结构，没有新增竞争部署的 workflow。完整 Pages 设置 API 未经认证返回 404，不能据此断言站点不存在；发布前在网页确认一次 Settings → Pages 的现有来源。

1. 查看本地修改和缺项记录，确认需要公开的 CV 内容；保持仓库名 `Melon-Xu.github.io`、URL 和空 `baseurl` 不变，Custom domain 留空，不添加 CNAME。
2. 重新构建并检查：`./scripts/site build`、`python3 scripts/check_site.py`。
3. 核对 `git status --short`，只提交站点源文件、本人 CV、维护文档和锁文件，不能提交 `_site/`、`local/` 或 `vendor/`。可使用：

   ```sh
   git add .gitignore Gemfile Gemfile.lock _config.yml README.md THIRD_PARTY_NOTICES.md \
     _data/profile.yml _data/experience.yml _data/research.yml _data/news.yml \
     _data/publications.yml _data/service.yml _includes/light-*.html \
     _layouts/minimal-light.html index.html 404.html publications cv assets/site.css \
     assets/site.js assets/favicon.svg assets/images assets/teasers \
     MeilongXu_Resume.pdf licenses docs scripts
   git diff --cached --stat
   git commit -m "Refactor academic homepage with Minimal Light and verified research updates"
   ```

4. **需要同步远端重构分支时执行（推送该分支本身不发布网站）**：

   ```sh
   git push -u origin codex/minimal-light-refactor
   ```

   在 GitHub 创建 PR 到 `master`，检查差异后合并（建议 squash 成一个易回退的提交）。合并会触发现有 Pages 发布；不要在未准备公开时合并。

5. 在 Settings → Pages 确认现有分支发布为 `master` / `(root)`，保持原配置。若当前显示 GitHub Actions，先确认现有动态 Pages 构建能处理根目录 Jekyll；不要另外启用重复 workflow。观察 Actions 中 `pages-build-deployment` 成功。
6. 打开 <https://melon-xu.github.io/>，强制刷新并核对首页、`/publications/`、`/cv/`、CV 下载和旧 slides/poster URL。公开站点检查只能在真正发布后执行，本次未声称线上验收。

GitHub 官方来源：[配置 Pages 发布来源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

## 回退

无需改写 Git 历史。基线提交可随时只读检查：

```sh
git show 87d6fdd713f61b878d5ee3aca8e7dd2a6af2a412:_config.yml
git diff 87d6fdd713f61b878d5ee3aca8e7dd2a6af2a412
```

如以后已发布，针对本次 squash 提交在新分支执行 `git revert <本次重构提交SHA>`，通过 PR 合回 `master`，由原 Pages 流程重新部署。也可使用 GitHub PR 的 Revert 功能。不要 `reset --hard` 或 force push；注意新简历原本为未跟踪文件，回退前保留副本。
