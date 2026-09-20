# 真人短剧导演生产技能包 v3.0

本包只保留三个可独立安装的生产 Skill，不再附带损坏的完整上游仓库快照：

1. `short-drama-storyboard`：Source Truth、关系Beat、观众信息、空间调度、连续性、冻结关键帧。
2. `short-drama-emotion-translate`：动态情绪预算、可见行为链、对手反作用、运镜触发与余波。
3. `short-drama-video-prompts`：把已确认分镜降维成文生或图生视频提示词，并处理声音、口型和模型执行档。

## 推荐调用顺序

普通分镜直接调用 `$short-drama-storyboard`。只有强情绪、表演修复或情绪运镜联动任务才加载
`$short-drama-emotion-translate`。分镜确认后再调用 `$short-drama-video-prompts`，下游只继承和压缩，禁止二次放大。

## v3.0生产更新

- 用关系Beat而非情绪音量判断戏剧推进。
- 新增观众信息、功能区域、物理母状态、道具状态机和独立声音时间线。
- 新增结构化镜头契约和跨镜机器校验，检查动作容量、长镜理由、母状态、道具与人物交接、VO口型和空镜纯净度。
- 新增Seedance中文执行档，支持只交付可复制正文。
- 新增失败码、冻结成功变量与单变量修复流程。
- 移除具体剧本人物、场景与资产，把项目经验降级为通用机制。
- 取消仓库内副本与独立副本并存，`skills/`是唯一Master。

## 验证

在包根目录运行：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_package.py
```

验证通过只证明文件结构、接口契约和结构化规则成立，不代表任何视频模型已经实测通过。未经真实生成的模型能力应标记为 `TEST_REQUIRED`。
