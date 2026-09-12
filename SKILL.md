---
name: hdrs-director-fusion
description: Relationship-first AI short-drama directing and storyboard skill for female-led trauma, marriage power conflict, restrained revenge, elite-family spatial oppression, ensemble relationship staging, and commercial vertical drama. Use when turning an approved script into director analysis, HDRS relationship beats, blocking, shot design, camera language, performance direction, Seedance-ready generation units, or storyboard QA. It routes each scene to functional directing modules inspired by controlled precision, spatial power, subjective trauma, social constraint, suppressed rage, and architectural alienation without mechanically copying a named director.
metadata:
  author: zhangzhen-hue
  version: "1.0.0"
  language: zh-CN
  method: HDRS
---

# HDRS Director Fusion

把剧本中的事件、台词和动作，转译成以“关系变化”为最小单位的电影化分镜。先理解戏剧关系，再设计人物调度，再选择摄影机，最后编译为 AI 视频可执行提示词。导演风格不得先于戏剧关系存在。

## Use When

使用本 Skill，当用户要求以下任一工作：

1. 对女性创伤、婚姻权力、冷静复仇、豪门家庭、身份羞辱、情感控制等关系型剧情做导演解读。
2. 把剧本拆成 HDRS 关系节拍、人物调度、镜头句、分镜表或 Seedance 生成单元。
3. 设计双人、三人、家庭群戏、礼貌型羞辱、压抑愤怒、创伤触发、权力翻转。
4. 检查现有分镜是否拖、是否机械正反打、是否只有情绪没有行为、是否缺少 Reaction 与关系余波。
5. 为竖屏海外女性向短剧做商业可读性、集尾 Hook、卡点与付费兑现检查。
6. 将已确认分镜翻译为 AI 视频生成提示词，同时保持人物站位、轴线、声音、道具、伤势和状态连续。

## Don't Use When

不要把本 Skill 当作：

1. 剧本改写器。用户未授权改编时，不改台词、剧情、人物身份、事件顺序和结局。
2. 单纯“导演风格模仿器”。不得先决定某位导演风格，再强迫所有场景套同一镜头语法。
3. 无剧情的产品展示、纯风景、纯舞蹈或工具演示的默认导演系统。此类任务可只使用非叙事摄影流程。
4. 纯影调、纯美术、纯服装或纯道具资产设计器。除非这些内容直接服务当前关系场。
5. 成片质量证明器。文字分镜通过 QA，不等于实际生成视频一定成功。

## Core Principle

本 Skill 的最高判断式：

> 镜头价值 = 可读的关系变化 × 可见行为 × 空间后果 × 时间清晰度。

分镜最小单位不是一句台词，而是一次有效关系变化。每个主要镜头至少承担一项：

- 权力变化
- 信息变化
- 亲密许可变化
- 社会身份变化
- 空间控制变化
- 选择变化
- 风险或代价变化
- 观众认知变化

如果删除一个镜头，剧情、关系、信息、行动因果或节奏都没有损失，默认合并、缩短或删除。

## Workflow

### Step 1：锁定事实边界

完整读取当前有效剧本与用户已锁定决定，区分四类信息：

- 剧本事实
- 用户锁定项
- 导演解释
- 尚未决定的拍法

只在真正会改变方案且无法从材料判断时追问一个关键问题。其余合理推导，但不得伪装成原文事实。

### Step 2：先做场景关系解读

每场先用一句话回答：

> 这场戏开始时谁控制谁，结束时谁控制谁，中间是什么动作或认知造成变化？

建立内部关系向量，按实际需要选择：

- Authority：命令、拒绝、打断、服从
- Intimacy：接近、触碰、许可、撤回
- Information：知道、隐瞒、识破、误判
- Social Legitimacy：家庭位置、公开身份、旁观压力
- Spatial Freedom：出口、通道、中心、边缘、移动自由
- Risk / Cost：谁承担风险，谁让别人付代价

不要为了完整而强填所有维度。

### Step 3：切成 HDRS 关系节拍

每个节拍写清：

`初态 → 刺激 → 第一 Reaction → 理解变化 → 结果动作 → 对方 Reaction → 新关系状态`

简单节拍可以压缩，但必须保留“前后状态差”。

优先识别人物真正做出的选择，而不是只识别情绪。女性向关系戏中，拒绝、留下、公开站队、收回资源、主动靠近、停止后退等行为通常比一句自我解释更有戏剧价值。

详见 [references/core-hdrs.md](references/core-hdrs.md)。

### Step 4：导演模块路由

每个场景最多指定一个主模块和两个辅模块。不要用百分比机械混合。

模块如下：

1. `CONTROL_PRECISION`：冷静控制、信息差、婚姻权力、精确观察。
2. `SPATIAL_POWER`：门、楼梯、纵深、站位、通道、高低位与关系翻转。
3. `SUBJECTIVE_TRAUMA`：身体记忆、感官触发、碎片式侵入、主观声音。
4. `SOCIAL_CONSTRAINT`：礼貌羞辱、观看关系、框中框、玻璃、家具和社会隔离。
5. `SUPPRESSED_RAGE`：疲劳、迟钝、防御、克制愤怒到恢复主动性。
6. `ARCHITECTURAL_ALIENATION`：人物被巨大空间吞没、豪华空间无归属感。只在关键节点低频使用。

模块只是一组功能语法。正式 AI 提示词优先输出可执行的摄影、调度和表演，不写“模仿某导演”。

六个功能模块的路由规则已在本文件中完整定义；研究来源见 [references/research-notes.md](references/research-notes.md)。

### Step 5：先调度，再摄影

先固定：

- 场景锚点
- 出入口
- 家具与障碍
- 人物站位
- 身体朝向
- 视线
- 道具归属
- 可通行路径
- 主关系轴
- 第三者观察轴

然后问：

> 人物怎样移动，才能让关系变化先在空间里发生？

只有人物调度清楚以后，才决定机位、景别、焦段、运动与剪辑。

### Step 6：形成镜头句

不要逐句台词机械切镜。先决定整段采用：

- 连续长镜
- 切分镜头
- 混合结构

镜头句必须有起点状态、关系变化过程和终点构图。

运动镜头必须写清：

`起始构图 → 画内触发 → 摄影机路径 → 速度变化 → 焦点或主体接力 → 终点构图`

若运镜不改变信息、空间关系或观看立场，就保持固定或删掉运动。

详见 [references/camera-axis-continuity.md](references/camera-axis-continuity.md)。

### Step 7：表演变成可见行为

禁止只写：

- 悲伤
- 愤怒
- 崩溃
- 震惊
- 隐忍

必须转成可拍行为，并符合角色专属反应语法。

重大刺激优先检查：

`听见 → 未完全理解 → 再确认 → 真正理解 → 控制或失控 → 做出选择`

强动作之后必须保留余波。亲吻、拥抱、拒绝、保护、扇耳光、摔物、公开站队之后，至少检查一次对方 Reaction 和新的关系结果。

创伤场、压抑愤怒与礼貌暴力详见：
[references/performance-and-trauma.md](references/performance-and-trauma.md)
与 [references/spatial-power-and-social-violence.md](references/spatial-power-and-social-violence.md)。

### Step 8：建立视觉角色弧

摄影机必须能随人物弧线变化，而不是全剧保持一个模板。

关系型女主可参考五阶段，但必须按剧本重算：

1. 被系统定义：边缘、门口、遮挡、被别人安排。
2. 观察系统：稳定中景、越肩、信息型特写，开始获得信息。
3. 进入系统：进入多人关系构图，成为结构变量。
4. 控制系统：女主移动以后，别人开始 Reaction。
5. 执行反击：镜头反而更稳定、更简洁，力量来自决定本身。

不要用“强者必仰拍、弱者必俯拍”的机械规则。

### Step 9：商业短剧门

仅当项目是海外竖屏商业短剧时启用。

检查：

- 前 3 秒是否至少包含关系、危险、异常、冲突或强视觉中的两项。
- 每 10 至 15 秒是否至少发生一次有效变化。
- 每集是否能用一句话说清“关系从哪里走到哪里”。
- 集尾 Hook 是否提出一个无法忽略的问题。
- 付费后是否先兑现上一集承诺，再建立新奖励。
- 关闭声音后，主要关系动作是否仍然大致可读。

详见 [references/vertical-drama.md](references/vertical-drama.md)。

### Step 10：编译 AI 视频执行稿

导演层与生成层分离。

导演层写“为什么这样拍”。

生成层只写模型能执行的：

- 人物和场景
- 起始状态
- 站位与视线
- 逐秒动作
- 台词与声音归属
- 景别、机位、焦段
- 摄影机起点与终点
- 速度与切点
- 表演动作
- 环境连续性
- 结束状态

当项目使用 Seedance 时，遵守用户当前锁定的生成时长和参考图规则。若当前项目未给时长，不虚构平台上限。

详见 [references/ai-video-execution.md](references/ai-video-execution.md)。

### Step 11：Director Score

交付前内部评分 100 分：

- 关系变化可读性 20
- 人物调度有效性 15
- 空间叙事 15
- 镜头必要性 10
- 表演与身体反应 10
- 信息控制 10
- 节奏与时间容量 10
- 商业可读性 5
- 视觉辨识度 5

关系变化低于 15 / 20 时，默认重做场景结构，而不是只换镜头术语。

评分规则已在本节完整定义。

## Output Modes

根据用户要求选择，不强制每次全部输出。

### Mode A：Director Read

输出：

1. 场景真正发生的关系变化
2. 起始关系图
3. 结束关系图
4. 主模块与辅模块
5. 关键调度策略
6. 视觉角色弧位置

### Mode B：Storyboard

推荐表格：

| 镜号 | 时长 | 关系任务 | 景别与机位 | 构图与站位 | 表演与动作 | 摄影机 | 声音 | 结束状态 |
|---|---:|---|---|---|---|---|---|---|

### Mode C：AI Execution

每个生成单元至少包含：

- 人物
- 场景
- 起始状态
- 人物站位
- 时间轴
- 台词 / O.S. / V.O.
- 摄影机执行
- 表演
- 同期声与环境声
- 结束状态
- 连续性锁

### Mode D：Audit

按镜头检查：

1. 删除后损失什么？
2. 关系有没有变化？
3. 动作有没有结果？
4. 对方 Reaction 有没有出现？
5. 空间和轴线是否连续？
6. 是否重复同一情绪？
7. 是否存在无动机运镜？
8. 是否超出 AI 生成单元容量？
9. 静音状态能否理解主要关系？
10. 下一镜是否从上一镜结果继续？

## Rules

1. 关系变化优先于镜头数量。
2. 调度优先于摄影机运动。
3. 人物行为优先于情绪形容词。
4. 对方 Reaction 与动作余波属于剧情，不是可有可无的装饰。
5. 站位、距离、遮挡、出口和道具控制都可以表达权力。
6. 固定镜头完全合法。摄影机不需要持续运动来证明“电影感”。
7. 复杂运动必须有画内触发和新的信息任务。
8. 景别不按固定远中近特顺序轮换。
9. 轴线来自人物或行动关系，换机位后重新计算屏幕方向。
10. VO 只承担画面无法完成的信息。VO 时可见人物不得假装口型。
11. 无台词人物不能木偶式静止，但微动作必须有原因，并符合当前景别。
12. 群演有活动基线、接收条件和反应时差，不统一同时转头。
13. 重要物理动作遵守“接触 / 受力 / 结果 / 余势”因果。
14. 道具、持物、伤势、位置和情绪残留不能在切镜后重置。
15. 豪宅、门、楼梯、玻璃、镜子和家具只有在改变关系可读性时才进入构图设计。
16. 反派不默认靠吼叫和狰狞表情成立。礼貌、等待、忽视、替别人决定同样可以构成暴力。
17. 创伤不默认等于哭泣。身体对声音、空间、触碰和出口的反应更优先。
18. 复仇不默认等于英雄仰拍。真正的翻转是别人开始对主角的决定产生 Reaction。
19. 导演参考只用于内部路由。正式生成提示词优先使用功能语言，不堆导演名字。
20. 未授权时不新增剧情、人物、台词、道具和结果。

## Examples

简例：

剧本事件：丈夫越过刚出狱的妻子，直接抱起另一个家庭中的孩子。

错误拆法：
“妻子特写难过。丈夫中景走路。孩子特写开心。”

HDRS 拆法：
“妻子原本仍期待丈夫停下 → 丈夫经过她时不停步 → 她肩背出现一次本能准备被拥抱的微动作 → 丈夫越过她抱起孩子 → 妻子没有追上去，视线停在丈夫与孩子形成的新家庭构图 → 她第一次确认自己已被排除在家庭身份之外。”

镜头任务不是拍三个人各自的表情，而是拍“家庭身份发生公开转移”。

上面的婚姻权力示例就是本版本的最小运行样例。

## Edge Cases

### 用户已经锁定镜头

保留锁定内容，只补足缺失的关系任务、空间、连续性和执行信息，不重新导演无关镜头。

### 用户只要 Seedance 提示词

内部仍完成关系、调度和连续性检查，但正文只交付可复制执行稿，不附长篇理论。

### 剧本本身没有关系变化

不要强造反转。判断它是否是必要的建立、观察、过程或过渡镜头；若不是，建议压缩。

### 多人群戏

先锁主关系轴，再锁第二关系轴与观察关系。每个时间点只允许一个主视觉焦点，其他人物保留异步 Reaction。

### 创伤闪回

默认不用完整回忆段。先尝试声音桥、物件匹配、0.3 至 1.5 秒感官碎片、同动作匹配或空间侵入。只有剧情需要完整信息时才扩成长闪回。

### 建筑异化

仅在空间本身需要成为制度压力、阶级边界或孤立证据时启用。普通对话不滥用超广角。

## References

运行时按需读取：

- [references/core-hdrs.md](references/core-hdrs.md)
- [references/performance-and-trauma.md](references/performance-and-trauma.md)
- [references/spatial-power-and-social-violence.md](references/spatial-power-and-social-violence.md)
- [references/camera-axis-continuity.md](references/camera-axis-continuity.md)
- [references/vertical-drama.md](references/vertical-drama.md)
- [references/ai-video-execution.md](references/ai-video-execution.md)
- [references/research-notes.md](references/research-notes.md)

研究依据与外部资料只用于解释本 Skill 的设计来源，不应机械复制成镜头公式。
