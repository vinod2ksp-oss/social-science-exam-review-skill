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

## GitHub 推送

如果仓库是新创建的，解压压缩包内容后在该目录执行：

```bash
git init
git add .
git commit -m "Add two-pass exam review skill"
git branch -M main
git remote add origin https://github.com/你的用户名/你的仓库名.git
git push -u origin main
```

如果已有 Git 仓库，把 `.agents/skills/two-pass-exam-review/` 复制进仓库根目录，执行：

```bash
git add .agents/skills/two-pass-exam-review
git commit -m "Add two-pass exam review skill"
git push
```

**Windows 用户注意：** `.agents` 是以英文句点开头的目录，解压后如果文件管理器不容易找到，可在 PowerShell 通过 `Get-ChildItem -Force` 检查。

## 如何调用

在支持技能的 Codex 中输入 `$two-pass-exam-review`，并带上课程和目标。例如：

```text
$two-pass-exam-review
继续产业经济学的第二轮复习。请先读取 state/industrial-economics-2026.md。
我已上传老师的95页PDF，先做第二至四章材料题专项补弱，再进入第五章。
```

或：

```text
$two-pass-exam-review
第一轮从第二章第一节开始，依照老师PPT，一次完整学习一节，闭卷测试满分10分，8分通过。
```

技能也可在支持 `@` 选择 Skill 的 ChatGPT 环境中通过选择器调用，具体可用性取决于所使用的产品和是否安装。

## 重要说明

- 仓库只保存**复习工作流与进度**，**不保存教师的原始95页PPT/PDF**。新聊天时应上传或提供可读取的课件；Skill 不能替代材料本身。
- 当前产业经济学的第1—4章第二轮测试已通过，但第二至四章综合材料题未完成，已记录在进度文件。
- 不依赖外部 Python 包；可使用随附脚本检查结构和核心文件。

## 自检

```bash
python .agents/skills/two-pass-exam-review/scripts/check_skill.py
```
