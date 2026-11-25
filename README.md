# 两轮递进式期末复习 Skill

面向社科类大学课程闭卷期末的 Agent Skill，适用于 Codex（CLI / IDE / 桌面端支持 Skill 的环境）和其他兼容 [Agent Skills](https://agentskills.io/specification) 格式的运行环境。

本仓库默认直接在根目录提供 `.agents/skills/two-pass-exam-review/SKILL.md`，适合直接推送 GitHub，并在该仓库的 Codex 环境中调用。

## 两轮模式

| 模式 | 学习节奏 | 产出 |
|---|---|---|
| 第一轮：课件逐节复习 | 整节讲完再闭卷测一次（≥8/10通过） | 知识体系、A/B/C笔记、考点表、闭卷题与评分 |
| 第二轮：按章应试复习 | 整章逻辑 → 名词解释/简答章测 → 跨章材料题 | 全书主线、章间逻辑、标准答题骨架、综合材料批改 |
| 第二轮补弱：材料题专项 | 事实 → 理论 → 机制 → 结论，短材料递进 | 新材料、单项练习、针对性批改，再返回综合题 |

## 仓库结构

```text
.
├── README.md
└── .agents/
    └── skills/
        └── two-pass-exam-review/
            ├── SKILL.md
            ├── agents/openai.yaml
            ├── references/
            │   ├── round-one.md
            │   ├── round-two.md
            │   └── grading.md
            ├── templates/
            │   ├── COURSE_PROFILE.md
            │   └── PROGRESS.md
            ├── state/
            │   └── industrial-economics-2026.md
            └── scripts/
                └── check_skill.py
```

## 如何调用

在支持技能的 Codex 中输入 `$two-pass-exam-review`，并带上课程和目标。

