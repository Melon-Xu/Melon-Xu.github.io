# Meilong Xu 个人主页

原网址保持为 **https://melon-xu.github.io/**。Jekyll 3.10 + 本地 Minimal Light 适配，无前端框架、远程主题、远程字体或追踪脚本。

```sh
./scripts/site install
./scripts/site build
python3 scripts/check_site.py
./scripts/site serve
```

预览：<http://127.0.0.1:4000/>。当前机器已配置隔离的 Ruby 3.4.5，脚本自动识别；其他机器请先安装 Ruby 3.2+ 与 Bundler 2.6.9。生产构建写入 `_site/`，预览单独写入 `local/preview/`。

- [内容维护说明](docs/MAINTENANCE.zh-CN.md)
- [事实来源、差异与缺项](docs/CONTENT_AUDIT.zh-CN.md)
- [检查结果与原域名发布步骤](docs/DELIVERY.zh-CN.md)
- [主题来源与授权](THIRD_PARTY_NOTICES.md)

只维护新 `_data/*.yml` 和 `light-*` 模板。旧 `_pages/` 等 Academic Pages 源文件保留作历史参考，已排除发布，不再编辑它们更新网站。原 PDF、slides、poster 和图片资源路径保留。
