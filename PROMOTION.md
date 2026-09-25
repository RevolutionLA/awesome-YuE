# 推广执行手册 · Promotion Playbook

> 目标：让 awesome-YuE 从"一份写得不错的清单"变成"YuE 生态的默认入口"。
> 状态：内容已就位（70+ 条目、中英双语、CC0），53 个收录仓库已通知完毕（见 [NOTIFICATIONS.md](NOTIFICATIONS.md)）。接下来的问题只有一个：**让人发现它**。

---

## 0. 先想清楚：awesome-list 是怎么死的

99% 的 awesome-list 死在同一个地方——**不是内容不好，是没人知道它存在**。

所以"把 README 排版做得更漂亮"是低杠杆动作。真正决定成败的只有三件事，按杠杆从高到低：

| # | 动作 | 类型 | 为什么杠杆高 |
|---|---|---|---|
| 1 | **被引用**：官方 README / HF 模型卡 / 第三方文档反向链接过来 | 一次投入，持续收益 | 一条权威外链 = 长期自然流量 + GitHub SEO 权重，胜过发 100 条帖子 |
| 2 | **被检索到**：仓库 topics、About、awesome 索引站收录 | 被动获客 | 零成本，设一次管几年；搜索"开源 Suno""本地 AI 音乐"的人会自己找上门 |
| 3 | **被转发**：把清单里的隐性知识做成独立内容 | 主动传播 | 清单本身不好传播，"我踩完坑的横评"才好传播 |

> ⚠️ 顺序不能反。先发社区帖子、后补反向链接，等于把流量倒进一个还没准备好的池子。

**受众画像（决定去哪儿推）**：YuE 被称为"开源版 Suno"，所以最精准的人群不是 AI 研究者，而是**想本地跑、不想付 Suno 订阅费、或想接进 ComfyUI/DAW 工作流的音乐爱好者与创作者**。他们聚集在 ComfyUI 社区、r/SunoAI、本地 LLM 圈和 B 站/知乎的 AI 音乐话题下——不是 arXiv 读者。

---

## 1. 阶段一：仓库自身配置（30 分钟，长期生效）

这一步零成本、不依赖任何人审核，**必须最先做**。

### 1.1 GitHub Topics（仓库页 → About → ⚙️）

建议填（GitHub 会按 topic 做探索页推荐和站内搜索）：

```
awesome  awesome-list  yue  yue2  music-generation  ai-music
text-to-music  lyrics-to-song  suno-alternative  local-llm
comfyui  mlx  song-generation  open-source-ai
```

### 1.2 About 描述与 Website

- **Description**：`🎵 Curated list of the YuE / YuE2 open-source music generation ecosystem — UIs, quantization, ComfyUI nodes, Mac/MLX ports, cloud serving & tutorials. 70+ projects.`
- **Website**：留 `https://github.com/RevolutionLA/awesome-YuE`（若将来做 GitHub Pages 站点再改）

### 1.3 Social Preview 图

仓库页 → Settings → Social preview → 上传一张 1280×640 的卡片图。分享到 X/微信/Reddit 时会直接显示缩略图，**这是转发率最低成本的提升手段**。

### 1.4 首屏钩子（已完成）

README 顶部已有「🚀 快速选择 Quick Picks」决策表——这是全篇最可能被截图转发的部分，也是"3 秒内让读者知道这清单对我有用"的关键。后续每次扩充分类，同步更新这张表。

---

## 2. 阶段二：拿反向链接（最高杠杆，重点投入）

### 2.1 官方仓库 `multimodal-art-projection/YuE` ⭐⭐⭐

**不要只发 Issue，要提 PR。** PR 比 Issue 的转化率高一个量级——维护者只需点合并。

操作：
1. Fork 官方仓库，在 README 的 "Community" / "Ecosystem" 段落**追加一行**（不要改动其他内容，降低合并阻力）：
   ```markdown
   - [awesome-YuE](https://github.com/RevolutionLA/awesome-YuE) — Community-curated list of 70+ YuE / YuE2 ecosystem projects: UIs, quantization, ComfyUI nodes, Mac ports, serving and tutorials (CC0, EN/CN).
   ```
2. PR 标题：`docs: link community-curated awesome-YuE list`
3. PR 正文（**重点是"我做过什么"而不是"请帮我"**）：

```markdown
Hi! The community has built a lot around YuE/YuE2 — GUIs, exl2/INT8/GGML runtimes, ComfyUI nodes, Apple Silicon MLX ports, serverless templates, LoRA trainers — but they're scattered across GitHub and hard to discover.

I've been maintaining a curated, bilingual (EN/CN), CC0 list of 70+ of them, with inclusion criteria and quarterly link checks:
https://github.com/RevolutionLA/awesome-YuE

This PR adds a single line to the README linking it. Happy to adjust the wording or placement, and I'll keep the list updated. If you'd rather I open a Discussion instead, just let me know.

Thanks for releasing YuE/YuE2 — it's a great model to build around. 🎶
```

4. **若 3 天无回应**：转发到 Discussions 的 Show and tell，并顺手回答 2–3 个其他人的问题再提一次（先混脸熟，再提请求，成功率显著更高）。

### 2.2 Hugging Face：m-a-p 组织与模型卡 ⭐⭐⭐

- 在 [YuE2-3B 模型卡](https://huggingface.co/m-a-p) 页面的 **Community** 区发 Discussion（不是 PR，HF 模型卡 PR 门槛高）；
- 文案见 §4.3；
- 顺带在 `YuE-s1-7B-anneal-en-cot`、`YuE-s2-1B` 等下载量高的模型卡下也留一次（不要同日发完，分几天）。

### 2.3 comfyui-wiki.com ⭐⭐（容易被忽略的高价值目标）

该站点已发布 [YuE2-3B 介绍与原生支持](https://comfyui-wiki.com/en/news/2026-09-11-yue2-3b) 一文——**流量精准且文章已存在**。联系站长，请求在文末加一句：

```text
Looking for more YuE2 tools? The community maintains an awesome-list here:
https://github.com/RevolutionLA/awesome-YuE
```

同理适用于任何已写过 YuE 的第三方博客/文档站——**找已有流量的人借力，比自己造流量快得多**。

### 2.4 awesome 索引站提交 ⭐⭐

| 站点 | 方式 |
|---|---|
| [LibHunt](https://libhunt.com) | Submit a project，选 Awesome Lists 分类 |
| [awesomeindex.org](https://awesomeindex.org) | 提交表单 |
| GitHub topic 探索页 | 靠 §1.1 的 topics 自动生效，无需提交 |

### 2.5 让收录项目反向链接 ⭐⭐

你已通知 53 个仓库。**下一步比通知本身更重要**：请对方在 TA 的 README 里加一句
`Listed in [awesome-YuE](https://github.com/RevolutionLA/awesome-YuE)`。

53 条高质量 backlink 的 SEO 效果远超任何单篇帖子。可在通知 issue 里追加一条回复（一次性，别刷屏）：

```markdown
Small follow-up: if you find the list useful, adding a line like
"Listed in [awesome-YuE](https://github.com/RevolutionLA/awesome-YuE)" to your README
helps others discover the ecosystem (and your project). Totally optional — thanks again! 🎶
```

---

## 3. 阶段三：把知识做成内容（可转发的载体）

**清单不好传播，文章好传播。** 把清单里的隐性知识抽出来写成独立内容，文末统一引流到仓库。

高潜力选题（按传播力排序）：

1. **《2026 本地跑 YuE2 全方案横评：8GB / 16GB / 24GB 显存各该怎么选》** — 最强选题。素材你全都有（显存速查、量化方案、GUI 对比），别人写不出来。
2. **《不想付 Suno 订阅费？开源替代 YuE2 的完整本地部署指南》** — 直击最精准人群与搜索词。
3. **《Mac 上跑 YuE2：MLX 移植现状》** — 受众窄但极精准，中文资料几乎空白。
4. **《把 YuE2 接进 ComfyUI：从原生节点到 LoRA 训练》** — ComfyUI 社区体量大、转发意愿高。

分发渠道：知乎（长文）、B站（视频/专栏）、即刻/V2EX（短文）、Reddit（英文版）、X（英文版）。每篇文末统一放一句：

```text
完整生态清单（70+ 项目，持续更新）：https://github.com/RevolutionLA/awesome-YuE
```

---

## 4. 阶段四：社区分发文案

> 原则：**以分享资源的口吻，不要刷屏或群发广告**。在社区里回答真人问题、顺带给出链接，效果远好于硬广。

### 4.1 Reddit（r/LocalLLaMA、r/comfyui、r/SunoAI、r/aimusic）

**标题：** `I made an awesome-list for the YuE / YuE2 music model ecosystem (UIs, quantization, ComfyUI nodes, Mac ports)`

```text
Since YuE2 dropped, a bunch of great community tools have scattered across GitHub — I kept losing track of them, so I curated them into one list:

https://github.com/RevolutionLA/awesome-YuE

What's inside:
- GUIs that run on modest hardware (YuEGP for GPU-poor, 8GB VRAM quantized UIs)
- ExLlamaV2 / INT8 / GGML quantized runtimes, incl. a pure C++ yue2.cpp build
- Apple Silicon MLX ports and native Mac apps
- ComfyUI node packs + the official native YuE2 nodes
- Cloud/serverless templates (RunPod, Cog, SaladCloud) and LoRA trainers

There's also a "Quick Picks" table at the top — pick by your VRAM and platform instead of reading 70 rows.

It's CC0 licensed, bilingual (EN/CN), and open for PRs. Feedback and missing projects very welcome!
```

**时机**：周末美东上午发流量最好。r/SunoAI 发帖前先读版规，部分版块禁自我推广。

### 4.2 X / Twitter

```text
The YuE / YuE2 ecosystem is exploding 🎶 so I curated everything into one awesome-list:

GUIs · quantized runtimes · ComfyUI nodes · Mac MLX ports · cloud serving · tutorials

Start here if you're not sure which one to use 👇 (Quick Picks table)
⭐ https://github.com/RevolutionLA/awesome-YuE

PRs welcome — missing something? Open an issue!
#AI_music #YuE #opensource
```

配图用 §1.3 的 social preview 图，或直接截「Quick Picks」表格。

### 4.3 Hugging Face（m-a-p Community Discussion）

```text
Hi! I maintain a curated ecosystem list for YuE / YuE2: UIs, quantization, ComfyUI nodes, Mac ports, serving templates and tutorials.

https://github.com/RevolutionLA/awesome-YuE

Feel free to link it from the model card if you find it useful — happy to take feedback or requests.
```

### 4.4 Discord（ComfyUI / LocalLLaMA / AI 音乐类服务器）

在 `#showcase`、`#ai-music` 频道简短发：

```text
Hey! I keep an awesome-list of YuE / YuE2 tools (GUIs, quantization, ComfyUI nodes, Mac ports): https://github.com/RevolutionLA/awesome-YuE — useful if you're running YuE locally. Suggestions welcome!
```

### 4.5 中文社区（知乎 / B站 / 即刻 / V2EX）

**标题：** `整理了一份 YuE / YuE2 开源音乐生成生态的精选清单（本地"开源版 Suno"）`

```text
YuE 是 m-a-p 团队开源的全曲生成模型（歌词直出完整人声+伴奏歌曲），社区衍生工具很多但比较分散，我整理了一份持续维护的清单：

https://github.com/RevolutionLA/awesome-YuE

内容包括：低显存 GUI（8GB 也能跑）、exl2/INT8/GGML 量化方案、ComfyUI 节点、Mac MLX 移植、云部署模板、LoRA 训练器和提示词最佳实践。

开头有张"快速选择"表，按你的显存和平台直接对号入座，不用翻完 70 行。

中英双语，CC0 协议，欢迎 PR 补充。
```

---

## 5. 执行节奏与衡量

**第 1 周（基建 + 最高杠杆）**
- [ ] 配置 topics / About / social preview（§1）
- [ ] 向官方仓库提 PR（§2.1）
- [ ] HF 模型卡 Discussion（§2.2）

**第 2–3 周（外链 + 首篇内容）**
- [ ] comfyui-wiki 站长触达（§2.3）
- [ ] 索引站提交（§2.4）
- [ ] 53 个已通知仓库追加 backlink 请求（§2.5）
- [ ] 写出并发布横评文章（§3 选题 1）

**第 4 周起（分发）**
- [ ] Reddit → X → 中文社区，每周 1–2 个渠道，不要同日全发

**衡量指标**（每周看一次，看趋势而非绝对值）

| 指标 | 在哪看 | 说明 |
|---|---|---|
| Star 增量 | GitHub Insights → Traffic | 判断哪次推广真正有效 |
| 访问来源 | Traffic → Referring sites | 反推哪个渠道带来流量 |
| 外链数 | GitHub 搜索 `"awesome-YuE" -repo:RevolutionLA/awesome-YuE` | 北极星指标 |
| Inbound PR / Issue | Issues | 清单是否进入"社区自转"状态 |

> **真正的成功标志**：开始有人主动提 PR 补充条目。到那一步，清单就从"你的项目"变成"社区的基础设施"，推广成本会自己降到零。

---

## 6. 注意事项

- 每个外部仓库**只开一个** issue，标题统一带 `awesome-YuE` 前缀，便于对方识别与搜索；
- HF 权重类条目（Doctor-Shotgun、Alissonerdx 等）没有 issue 区，改用 HF Community Discussion 或跳过；
- 一次发太多 issue 可能被判定为 spam，分几天、每批 ≤10 个；
- 对方要求下架时，24 小时内移除并回复确认（邮箱：liuang0307@foxmail.com）；
- **不建议**为推广而堆砌条目——收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)，可信度是这份清单唯一的资产。
