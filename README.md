# huabao · 华为画报 Skills

华为画报内容策划、标题打磨、栏目生产与曝光统计的统一维护仓库。当前推荐日常策划入口：**huabao-content-master v1.1.0**，以对应品类原始标题参考校准选对象和标题，重视网感、吸睛、信息密度及真实兑现。图片适用性由用户人工复核。

## 按工作选择

| 分类 | Skill | 用途 |
|---|---|---|
| 日常策划 | [huabao-content-master](skills/huabao-content-master/SKILL.md) | 新题、换弱题、短标题、四项题卡及策划复盘；各品类参考机制参与最终选择 |
| 日常策划 | [huabao-topic-studio](skills/huabao-topic-studio/SKILL.md) | 对象发现、标题竞争、原文证据与四项题卡的工作室流程 |
| 综合治理 | [huabao-content-planner](skills/huabao-content-planner/SKILL.md) | 原有综合策划、数据口径、正式审核与知识库流程 |
| 旅行 | [huabao-travel-content-planner](skills/huabao-travel-content-planner/SKILL.md) | 旅行专项策划及正式候选审核 |
| 旅行 | [travel-headline-refiner](skills/travel-headline-refiner/SKILL.md) | 已有旅行事实的标题与副标题打磨 |
| 明星 | [huabao-star-topic-planner](skills/huabao-star-topic-planner/SKILL.md) | 明星新选题与证据、舆情、概念去重 |
| 明星 | [huabao-star-headline-refiner](skills/huabao-star-headline-refiner/SKILL.md) | 已有明星标题与文案改写 |
| 栏目 | [weekly-intel-station](skills/weekly-intel-station/SKILL.md) | 一周情报站五条轻资讯栏目 |
| 数据 | [huabao-exposure-stats](skills/huabao-exposure-stats/SKILL.md) | 固定结构内容明细的正曝光周期与副本统计 |

目录保持并列，以兼容原有专项Skill的兄弟目录引用。分类通过本导航提供，不随意移动模块破坏依赖。原专项保留其工作范围；用户最新指令优先，Master的人工图片分工不会偷偷改写其他Skill。

## 使用

将所需 `skills/<skill-name>/` 目录复制到本机Codex Skills目录；需要共享治理的专项，请一并复制 `huabao-content-planner`。也可一次复制 `skills/` 下全部9个目录。

```text
使用 $huabao-content-master，结合最新素材策划5个旅行选题，按标题、副标题、单段论据摘要和原文链接输出。
```

运行时优先用户本次素材、对应品类原CSV与实际历史/近期记录。Master随包参考快照仅用于风格机制和记录核对，不证明事实、当前热点或发布条件。

## 维护与迁移

- 统一在本仓库维护；[迁移对应表](docs/migration.md)记录8个旧仓库与新目录。
- 旧仓库保留完整Git历史，增加新入口后归档；旧链接可读，后续更新使用本仓库。
- [旧版明星策划](legacy/huabao-star-content-planner/SKILL.md)留作历史兼容资料，当前新题优先用 `huabao-star-topic-planner` 或Master。不将旧版重复名称混入日常安装目录。
- [验证说明](docs/validation.md)区分结构、编码读取、风格复测和真实选用反馈；机械通过不证明标题吸睛。
- 不提交原始曝光工作簿、历史已做/上传数据库、月报全文、私有聊天全文或账号凭据。
