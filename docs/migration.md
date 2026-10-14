# 画报仓库迁移对应

迁移日期：2026-10-14。9个当前Skill集中在 `skills/`，一个旧版明星策划保留在 `legacy/`。9个当前目录不合并指令、不改名称，避免调用与共享引用失效。

| 旧仓库 | 统一目录 | 说明 |
|---|---|---|
| gravity0603/huabao-content-planner | skills/huabao-content-planner | 当前已发布综合版本，与本地当前文本一致 |
| gravity0603/huabao-exposure-stats | skills/huabao-exposure-stats | 当前曝光统计版本 |
| gravity0603/huabao-travel-content-planner | skills/huabao-travel-content-planner | 当前已发布旅行版本，与本地当前文本一致 |
| gravity0603/travel-headline-refiner | skills/travel-headline-refiner | 采用已安装v1.3.1；旧仓库v1.1.0保留在旧Git历史 |
| gravity0603/huabao-stars | skills/huabao-star-topic-planner；skills/huabao-star-headline-refiner | 两个当前明星模块，保留各自目录 |
| gravity0603/huabao-star-headline-refiner | skills/huabao-star-headline-refiner | 旧单独仓库v1.0.0由当前v1.1.0模块承接 |
| gravity0603/huabao-star-content-planner | legacy/huabao-star-content-planner | 旧v1.0.0，作为历史资料；推荐当前明星模块 |
| gravity0603/weekly-intel-station | skills/weekly-intel-station | 一周情报站当前版本 |
| 本地huabao-topic-studio | skills/huabao-topic-studio | 本次首次集中发布，保留工作室自身流程 |
| 本地huabao-content-master | skills/huabao-content-master | v1.1.0，修正实测后标题参考对齐与对象筛选 |

旧仓库的Git历史仍在原仓库，不删除、不改写历史提交。本仓库保存当前可维护内容，旧仓库README给新入口，归档后不会继续形成多个维护位置。

公开/归档状态以实际GitHub仓库结果为准，不由此文自报成功。对应来源树与内容摘要记录在repository-map.json，验证结果见validation.md。
