# 05 信息源：素材入口、事实原文、图源与授权

研究日期：2026-10-14（Asia/Shanghai）。范围：华为画报内容策划，从用户素材库补齐原文核验与图片来源路径。本文件是 Phase 1 研究笔记，尚非最终操作系统。外部来源实际通过 web open/click 读取；没有将搜索摘要算作正文。日本相关选题对象、IP、人物和图源排除；国际机构页面的语言导航不构成选题对象。

## 本地语料先读结果

- 完整读取 `D:/yiyouliao working/工作内容/每周数据/数据库/zcy华为画报选题-素材库.csv`，表头为名称、类型、链接；143 条数据记录，不含表头。
- 130 条记录包含 http(s) 字符串；这不是 130 篇事实已验证的原文。9 条全空；其余 4 条无 URL 为备用、科技占位、杭州光棱文字、影视草稿。130 条中还包括正文 URL、账号主页和资源网站混合。
- URL 记录按类型文字多标签计数：明星 40、影视 34、旅行/旅游 31、萌宠/宠物/猫咪 29、科技/科学 23、动漫 9、美食 7、体育 4、艺术 3、座驾 3、历史 1。分类可重叠，不能相加当独立来源数。
- 同名重复：宠物家、中国国家地理景观、生命时报各 2 条；前者同账号不同参数，后两者不同平台，不能仅按名称全删。
- 清洗缺口：部分 URL 被中文括号包住；明星私服穿搭 daily 一格有两个 URL；“萌宠 ”尾部空格；“奇点科学杂志”“科普世界”类型为空；末尾有标题/正文混入账号表。只记录问题，未改用户源文件。
- CSV 无采集日期字段，不能用参数中的数字推断账号最近更新日期。“最新素材优先”应先定位用户最近新增/近期更新入口，再进入其最新正文核实。末尾混入内容的“预计 9 月播出”等说法未经验证，不能继承。
- 已完整读取本地 `huabao-topic-studio/references/source-map.md` 与 `category-playbook.md`。它们是用户工作机制、历史标题偏好的本地语料，不是外部事实证据。其规则支持四项卡片、品类差异和选定后精查图片；事实与授权仍须独立核验。
- 本任务起步时 `references/research/seeds/` 不存在；本地完整 CSV 作为可用 seed。本领域不为凑种子运行无关 arXiv/GitHub collector。

## 素材库入口如何用

| 本地入口例 | 用途 | 当前证据边界 |
|---|---|---|
| 中国国家地理景观、UU旅行、建筑师的植物园、Atlas Obscura | 发现可成像地点/建筑与异常细节 | CSV 账号/站点已读，账号新文章尚未逐一在线打开 |
| 喵和汪、狗狗鉴定家、猫拾三、宠物天空 | 找猫狗具体行为、主人故事与视觉钩子 | 账号条目本身不证明行为机制或视频原创权 |
| NASA Earth Observatory、科学旅行号、中科院物理所 | 找卫星画面、天文对象与机制问题 | NASA 下列入口和正文已打开；其余账号正文未逐条验证 |
| 人民文娱、腾讯娱乐、VOGUE、国漫最新动态 | 作品/人物/造型线索 | 必须追剧方、制作方、媒体原稿或本人公开输出；不能把传闻写定论 |
| 今日热榜、MSN 渠道页 | 找话题/跨站传播线索 | 热榜不证明事实；渠道页/转载不等于原文 |

master-skill 的外部研究本轮不使用知乎、公众号、百科作为事实源。这一研究范围限制不改写用户日常素材库，不将其中知乎账号或今后的公众号素材永久禁用；用户指定时仍先读其线索，再找可靠原文，并说明验证状态。

## 8 个实际打开的官方 seed

统一读取日期：2026-10-14。可信度“一手”指机构自己的条目、编辑原文或规则；官方编辑解释仍不能替代具体论文结论。分类的“已读取”不代表图片已查看、版权已核验或选题可上架。

| ID | 来源与原文链接 | 类型/可信度 | 读取发现与用途 | 更新方式与边界 |
|---|---|---|---|---|
| S01 | [UNESCO·The Jantar Mantar, Jaipur](https://whc.unesco.org/en/list/1338/) | 旅行建筑事实源；一手机构遗产条目 | 印度斋浦尔砖石天文装置、裸眼观测用途，有具体物体与机制。可从“建筑如何承担观测”找切口。 | 遗产条目按需更新；不是实时游览/开放信息。正文许可不等于页内照片许可。 |
| S02 | [Cornell·Cats that Lick Too Much](https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics/cats-lick-too-much) | 猫健康/行为事实源；一手机构科普 | 过度舔毛可能涉及瘙痒、疼痛，也可能涉及压力；须排除医疗问题后再考虑压力解释。支撑“可见动作→多种机制→适用边界”。 | 页面无清晰发表日期，不能称近期新闻。图存在不等于许可；不作个体诊断。 |
| S03 | [RSPCA·Understanding Your Dog's Behaviour](https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour) | 狗行为与福利事实源；一手机构指南 | 强调奖励训练、安全躲避空间、运动和游戏；适合纠正把恐惧/异常行为当搞笑的切口。 | 指南按需更新；个体年龄/健康限制需另核实；站内视频也要追原创和许可。 |
| S04 | [NASA·Earth Observatory](https://science.nasa.gov/earth/earth-observatory/) | 旅行/地理科技线索入口；一手机构资源 | 图像配地球系统解释，提供 Image of the Day、主题、订阅与 RSS 路径。优先从具体图和可解释反差进入。 | 官方描述每日图文；主页会变，正文发布日期与影像拍摄日期另记。 |
| S05 | [NASA·An Impact Structure With Legs](https://science.nasa.gov/earth/earth-observatory/an-impact-structure-with-legs/) | 旅行地貌/科技事实原文；一手机构编辑稿 | 澳洲 Spider Crater 放射状砂岩脊；2026-10-13 发稿、2026-09-20 Landsat 9 影像。成因解释连接冲击与侵蚀；撞击年代是估计范围，不能写精确年份。 | 有论文/会议等参考与图片署名、下载入口；本文原文核实完成，图未下载/精查，H/R/B 未做。 |
| S06 | [NASA·NASA Images and Media Usage Guidelines](https://www.nasa.gov/nasa-brand-center/images-and-media/) | 图片/媒体使用规则入口；一手官方规则 | 一般信息性使用与推广用途条件不同；第三方版权材料须找权利人；NASA 网页出现不自动传递授权。 | 制作时重查对应图署名、标志、可识别人物、实际用途；不直接宣称全部 NASA 图免费商用。 |
| S07 | [The Met·Open Access at The Met](https://www.metmuseum.org/hubs/open-access) | 艺术图片与数据授权入口；一手官方政策 | CC0 覆盖其开放公有领域作品图与基本数据；作品页 OA 标志可帮助筛图，并提供 API 等资源路径。 | 逐作品核实 OA/公有领域状态；政策不能推出所有馆藏图片均可用。 |
| S08 | [The Met·The Musicians](https://www.metmuseum.org/art/collection/search/435844) | 作品元数据/机构解说＋图片入口；一手馆藏条目 | 卡拉瓦乔 1597 年作品，页内标 Public Domain，有尺寸、藏品号、音频解说及图像入口；示范“具体作品→可见细节→馆方解释”的核验路径。 | 作为检索案例，不是最终选题；本作品有人体表现，需画报场景审核。未查看下载高清图，不能称已完成图片审核。 |

说明：S05 文章署名 Lindsey Doermann，图像署名 Michala Garrison，Landsat 数据来自 USGS；可供下一 wave 人物/工具追踪，但不据此宣称其为行业 top figure。S02 引用 Cornell 专家 Pamela Perry、William Miller；这些是专业核验切入点，不是已完成的独立背书。

## 未成功读取与研究缺口

- `https://www.nps.gov/yell/learn/nature/thermal-features.htm` 与 `https://www.dpm.org.cn/collection.html` 本轮 web open 返回不可访问；不计入 8 个已读 seed，不据搜索摘要作事实结论。
- 现有素材偏账号/转载和娱乐线索，独立的艺术/历史/体育专业源较少；猫狗机制应补学术论文或兽医机构，作品需补官方制作方、角色简介、近期播出状态。
- 未为凑数宣称“newsletter 前五/podcast 前五/会议前三”。锁屏日常策划更直接需要选题入口、事实原文与图源条目；NASA 有订阅/RSS 路径已看到，但未订阅；Cornell hub 提供 CatWatch Newsletter 链接，期刊频率未核实。
- 8 个 URL 仅 5 个独立机构/站点系统（UNESCO、Cornell、RSPCA、NASA、Met），不能当 8 个独立背书。没有“从业者普遍使用”的统计证据。
- 图源政策与图片逐件使用许可分开；用户本地素材读取完成不等于账号全量在线复核或跨批 H/R/B 完成。

## 下一 wave 可用信号

1. 信息源三层应固定区分：线索入口（账号/栏目/订阅）→可引用事实原文（论文/机构条目/官方作品页）→图片文件与使用规则。
2. 有价值的视觉事实必须同时记录对象、机制、时间口径、可见画面类型和未完成状态；卫星图不是游客现场照片。
3. 工具追踪 seed：NASA RSS/订阅、Landsat 9/OLI 与 USGS 数据、Met Open Access/Collection API、馆藏元数据/音频 transcript。
4. 含案例和叙事的官方正文比账号列表更能用于改标题与短摘要；主页只负责发现下一篇要读的正文。
5. 普通初筛可延后高清图片和授权精查，但输出须写准确缺口；不把尚未选定的候选包装成可上架。
