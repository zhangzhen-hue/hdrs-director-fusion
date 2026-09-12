# Research Notes

本文件记录 v1.0.0 的方法来源。研究材料只用于提炼可迁移的导演功能，不要求最终提示词模仿任何在世创作者。

## Agent Skills 架构

- Agent Skills specification: https://agentskills.io/specification
- agentskills/agentskills: https://github.com/agentskills/agentskills

采用的工程原则：
- SKILL.md 负责路由与主流程
- 详细知识拆到 references
- 按任务渐进读取
- name 与 description 保持明确可检索

## AI 分镜与视频 Skill 结构参考

- https://github.com/62656456/ai-film-skills
- https://github.com/Emily2040/seedance-2.0
- https://github.com/tuoxie0102/ai-director-skill

提炼的工程原则：
- 先理解剧情、人物目的和调度，再选摄影
- 连续性、轴线与生成单元独立检查
- 长故事全局规划，单生成单元局部执行
- 内部戏剧判断必须翻译成可见或可听的执行信息

## 导演语言研究

本版本把研究内容抽象为六类功能模块：
- CONTROL_PRECISION：稳定、信息控制、冷静权力
- SPATIAL_POWER：门、楼梯、纵深、通道与阵营
- SUBJECTIVE_TRAUMA：感官触发、身体记忆、短碎片侵入
- SOCIAL_CONSTRAINT：观看关系、框中框、礼貌型排斥
- SUPPRESSED_RAGE：压抑愤怒、身体代价、主动性恢复
- ARCHITECTURAL_ALIENATION：大空间、小人物、制度性压迫

外部研究重点包括 David Fincher / Jeff Cronenweth、Park Chan-wook、Jean-Marc Vallée、Todd Haynes、Karyn Kusama、Yorgos Lanthimos / Robbie Ryan 的公开访谈与摄影资料。

## HDRS 自有方法来源

本 Skill 的核心来自用户持续整理的：
- HDRS 高密度关系场分镜系统
- AI 短剧分镜导演规范
- 海外女性向推文短剧成片审片规则

核心继承：
- 关系变化优先
- 主轴与次轴
- Reaction 与动作余波
- 人物站位和空间权力
- VO 可见人物闭口
- 道具、伤势、动作因果与连续性
- 独立生成单元自包含
- 静音、截图、删除测试
