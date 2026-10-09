# GitHub README 工坊

面向 AI Agent 的可复用技能，用于创建或优化高质量 GitHub README：先确认语言，再梳理项目价值、制作可点击效果图、核验安装命令，并在公开发布前检查链接、资源与隐私风险。

## 核心能力

- 第一轮先让用户选择 README 的**主语言**和**可选语言**，不自行猜测。
- 从代码库、示例、构建文件与部署配置中核验项目描述、命令和链接。
- 生成首屏清晰、结构克制的 README，并为产品、报告或工具添加可点击视觉演示。
- 为交互式 HTML 等 GitHub Markdown 不能直接嵌入的内容，设计“预览图 → 完整在线示例”的阅读链路。
- 用合成或匿名化样稿替代个人研究、客户资料和本地工作内容。
- 检查相对链接、图片路径、常见本地路径与凭据模式。

## 使用方式

安装到 Codex：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/Zimzheng/github-readme-craft.git "${CODEX_HOME:-$HOME/.codex}/skills/github-readme-craft"
```

随后在任务中写：

```text
使用 $github-readme-craft 优化当前仓库的 README。
```

技能会先询问 README 的主语言与可选语言。

## 质量检查

校验 README 的标题、相对图片与链接、常见本地路径和凭据模式：

```bash
python3 scripts/validate_readme.py README.md --repo-root .
```

该检查验证可机械确认的交付条件；项目事实、视觉质量和外部链接可用性仍应由 Agent 结合实际项目与预览工具核对。

## 文件结构

```text
.
├── SKILL.md                         # Agent 工作流与边界
├── README.md                        # 人类使用说明
├── agents/openai.yaml               # Codex 界面元数据
├── references/readme-playbook.md    # README 信息架构与视觉演示规范
└── scripts/validate_readme.py       # 零依赖校验器
```
