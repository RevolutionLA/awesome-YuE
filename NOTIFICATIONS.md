# 收录通知模板 · Notification Templates

> 用途：Awesome YuE 收录新项目后，到对方仓库开一个友好通知 issue。
> 说明：本机未配置 GitHub 凭据（无 `gh` CLI / `GITHUB_TOKEN`），无法自动代发；请手动到各仓库 Issues → New Issue 粘贴以下内容。
> 原则：只发一条、语气客气、明确给出"调整/下架"出口与联系方式（592213965@qq.com）。

---

## 英文版（推荐，国际项目通用）

**标题 / Title:** `Your project is featured in awesome-YuE 🎵`

**正文 / Body:**

```markdown
Hi! 👋

I'm the maintainer of **[awesome-YuE](https://github.com/RevolutionLA/awesome-YuE)** — a curated list of the YuE / YuE2 ecosystem: UIs, quantized runtimes, ComfyUI nodes, local ports, cloud serving and tutorials.

I'm happy to let you know that **your project has been included** in the list:

- List entry: <在此粘贴 README 中对应条目的锚点链接>
- Repo: <owner>/<repo>

If you'd like the description adjusted, moved to another category, or removed entirely, just reply here or email **592213965@qq.com** — no questions asked.

If you find the list useful, a ⭐ or a link back is always appreciated but never required.

Thanks for building for the YuE community! 🎶
```

---

## 中文版（中文项目适用）

**标题：** `您的项目已被 awesome-YuE 收录 🎵`

**正文：**

```markdown
你好！👋

我是 **[awesome-YuE](https://github.com/RevolutionLA/awesome-YuE)** 的维护者，这是一份 YuE / YuE2 生态的精选清单（界面、量化加速、ComfyUI 节点、本地移植、云部署、教程等）。

很高兴通知你：**你的项目已被收录**：

- 条目位置：<在此粘贴 README 中对应条目的锚点链接>
- 仓库：<owner>/<repo>

如果希望修改描述、调整分类或**下架**，直接在本 issue 回复，或发邮件到 **592213965@qq.com**，我们会尽快处理。

如果觉得这份清单有用，欢迎点个 ⭐ 或互相加个链接（非必须）。

感谢你为 YuE 社区做的贡献！🎶
```

---

## 发送清单 Checklist（建议优先级）

| 优先级 | 仓库 | 说明 |
|---|---|---|
| ⭐⭐⭐ | timoncool/YuE2-Studio | 活跃 YuE2 GUI |
| ⭐⭐⭐ | deepbeepmeep/YuEGP | 官方推荐，受众广 |
| ⭐⭐⭐ | joeljuvel/YuE-UI | 官方推荐 |
| ⭐⭐⭐ | sgsdxzy/YuE-exllamav2 | YuE1 时代核心加速方案 |
| ⭐⭐⭐ | smthemex/ComfyUI_YuE | ComfyUI 社区最流行节点 |
| ⭐⭐ | filliptm/ComfyUI-FL-YuE2 | 活跃 YuE2 节点 |
| ⭐⭐ | ServeurpersoCom/yue2.cpp · engival/yue2.cpp | C++ 移植，话题性强 |
| ⭐⭐ | tonywestonuk/YuE-Studio · vanch007/mlx-Yue · ianiv/YuE2 | Mac 生态代表 |
| ⭐⭐ | NoizAI/YuE2-Turbo | 官方 README 推荐的服务化工具 |
| ⭐ | 其余表格中的项目 | 按活跃度分批，每批 ≤10 个，避免刷屏 |

**注意事项**
- 每个仓库**只开一个**通知 issue，标题统一带 `awesome-YuE` 前缀便于对方识别与搜索；
- HF 权重类条目（Doctor-Shotgun、Alissonerdx 等）没有 issue 区，用 Hugging Face 的 Community Discussion 代替，或跳过；
- 一次发太多 issue 可能被判定为 spam，建议分几天、每批 ≤10 个；
- 对方要求下架时，24 小时内移除并回复确认。
