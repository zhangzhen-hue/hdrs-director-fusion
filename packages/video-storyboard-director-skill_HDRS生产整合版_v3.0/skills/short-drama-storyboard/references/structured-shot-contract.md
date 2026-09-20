# 结构化镜头契约

普通单场可以只交付正式分镜Markdown。以下情况建议同时维护 `shot-contracts.jsonl`：整集批量生产、多模型转换、复杂道具、三人以上、持续物理状态、跨段VO或需要机器QA。

首行是 `contract_header`，其后每行一个 `shot`。最小字段见 `assets/shot-contract.example.jsonl`。

结构化契约不替代导演分镜，只记录机器检查需要的边界：

- Source refs和事件ID；
- 流职责与镜头职责；
- 完整Starting State和Ending State；
- 母状态；
- 一个主要动作、最多一个次级反应和一个Camera Idea；
- 声音类型、说话者、口型与跨镜职责；
- 长镜必要性和镜内注意力事件；
- 空镜中人物、人体局部、影子与倒影均不存在。

检查命令：

```bash
python3 scripts/production_contract_check.py path/to/shot-contracts.jsonl
```

检查通过不等于导演质量通过，也不等于目标模型已验证。它只负责暴露结构错误和跨镜状态断裂。
