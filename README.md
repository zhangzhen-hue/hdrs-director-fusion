# HDRS Director Fusion

面向关系型 AI 短剧的导演分镜 Skill。

核心定位：

> 以 HDRS 关系变化作为剪辑与调度单位，以控制、空间权力、主观创伤、社会约束、压抑愤怒和建筑异化六个功能模块组织导演语言，再编译为可执行的 AI 视频分镜与提示词。

## 适合的项目

- 女性创伤
- 婚姻权力关系
- 冷静复仇
- 豪门家庭
- 身份羞辱
- 女性向海外竖屏短剧
- 高密度三人 / 群体关系场
- Seedance AI 视频分镜

## 目录

```text
hdrs-director-fusion/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── core-hdrs.md
│   ├── director-router.md
│   ├── performance-and-trauma.md
│   ├── spatial-power-and-social-violence.md
│   ├── camera-axis-continuity.md
│   ├── commercial-vertical-drama.md
│   ├── ai-video-compiler.md
│   ├── qa-scorecard.md
│   └── research-notes.md
├── examples/
│   └── marriage-power-scene.md
├── tests/
│   └── smoke-test.md
└── scripts/
    └── validate_skill.py
```

## 设计原则

1. 剧情理解先于镜头术语。
2. 关系变化先于情绪特写。
3. 人物调度先于摄影机运动。
4. 导演参照按功能路由，不按百分比混搭。
5. 内部导演判断必须翻译为可见 / 可听行为。
6. Skill 主文件保持精简，复杂知识按需读取 references。
7. 商业短剧门是条件模块，不强行覆盖所有电影型任务。

## 安装

遵循 Agent Skills 目录约定。可把整个 `hdrs-director-fusion` 文件夹放入支持 SKILL.md 的 Skills 目录。

不同客户端的具体安装路径可能不同，以当前客户端文档为准。

## 测试

先跑 `tests/smoke-test.md` 的四个案例。

也可以运行：

```bash
python scripts/validate_skill.py
```

该脚本只验证目录、frontmatter 和文件引用等静态结构，不证明导演质量。

## 研究资料

详见：

`references/research-notes.md`

其中记录：
- Agent Skills 公开规范
- AI storyboard / Seedance Skill 的工程架构参考
- Fincher、Park Chan-wook、Jean-Marc Vallée、Todd Haynes、Karyn Kusama、Yorgos Lanthimos / Robbie Ryan 的访谈与摄影资料
- 用户自有 HDRS、短剧分镜与商业审片方法的融合原则
