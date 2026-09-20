# `motion-specs.jsonl` 填写模板

文件第一行是 `sources` 声明：每个上游快照在这里写一次 `owner`、`artifact` 和已接受的
`artifact`，后面的记录用它的 key 引用。key 用产物文件名派生的短小写名字，在本文件内稳定且唯一。
本阶段插入的片段（[`performance.fragment.json`](performance.fragment.json)、
[`coverage-scope.fragment.json`](coverage-scope.fragment.json)）落进同一个文件，它们用到的 key
也在这里声明。

```jsonl
{"record_type":"sources","schema_version":"1.0.0","sources":{"shots":{"owner":"short-drama-storyboard","artifact":"剧集/<EP>/storyboard/shots.jsonl"},"characters":{"owner":"short-drama-assets","artifact":"剧集/<EP>/assets/characters.jsonl"},"screenplay-index":{"owner":"short-drama-write","artifact":"剧集/<EP>/screenplay-index.jsonl"}}}
```

其后每行一个运动规格记录；同一 `shot_ref` 只写一条运动规格，所有引用都用文件头声明的 `src`：

```json
{
  "motion_id": "MOTION-<stable-id>",
  "status": "candidate",
  "shot_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>"
  },
  "accepted_duration_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/duration_seconds"
  },
  "accepted_duration": "<从 accepted_duration_ref 读到的值，投影不改写>",
  "direction": "<relative frame direction; if a subject-self direction is needed, name the subject explicitly>",
  "axis_side_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/axis_side"
  },
  "start_boundary_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/start_boundary"
  },
  "end_boundary_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/end_boundary"
  },
  "primary_action": "<单镜主要动作变化；必须落到 end boundary>",
  "secondary_reaction": "<可选，最多一项；没有就删除>",
  "camera_intent": "<单一主要运镜职责；无触发时写 fixed/locked intent，不额外加装饰运动>",
  "camera_movement": "<push | pull | pan | track | arc | handheld | locked；只能是已接受 camera_intent 的执行投影>",
  "motion_amount": "<small | medium | large；本镜动作/运镜体量，不改写剧情强度>",
  "event_cue": "<触发主运动的剧情事件或可见/可听信号>",
  "continuity_in_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/start_boundary"
  },
  "continuity_out_ref": {
    "src": "shots",
    "record_id": "SHOT-<id>",
    "field": "/end_boundary"
  },
  "performance_ref": "<可选：同记录 performance_arcs[] 的 actor_ref/trigger_ref 组合；没有就删除>",
  "attention_handoff_ref": "<可选：同记录 attention_handoffs[] 中对应的 from_ref/trigger_ref/to_ref；没有就删除>",
  "coverage_scope": "<可选：同记录 coverage_scope.fragment.json 的 side/orientation；不改变 axis_side>",
  "unresolved": [],
  "provenance": "storyboard_projection"
}
```

## 结构校验点

每条运动规格在落盘时满足以下条件；这是 `VID-12` 的本地可证部分：

1. `shot_ref`、`accepted_duration_ref`、`axis_side_ref`、`start_boundary_ref`、`end_boundary_ref`、
   `continuity_in_ref`、`continuity_out_ref` 都指向**同一条**镜头记录；
2. `accepted_duration` 与 `accepted_duration_ref` 解析到的镜头 `duration_seconds` 一致；
3. `continuity_in_ref == start_boundary_ref`，`continuity_out_ref == end_boundary_ref`；
4. `camera_movement` 只作为 `camera_intent` 的可执行投影，不得反向创造未接受运镜；
5. `motion_amount` 是执行体量，不得替代剧情、情绪或权力变化的上游依据；
6. `primary_action` 与最多一个 `secondary_reaction` 能在 `accepted_duration` 内完成；放不下时请求拆镜；
7. `event_cue` 必须来自已接受的剧情事件、动作触发、对白/声音触发或关系变化；没有触发时运镜保持 `locked`；
8. `unresolved` 非空时记录仍可保存为 candidate，但不得通过最终生成就绪 gate；
9. `sources` 头里每个被引用 key 只声明一次，且同 key 不得指向两个不同快照。

这些检查和容器检查互补：运动规格证明“本镜怎么动”，容器只证明“哪些已接受镜头装在一起”。
