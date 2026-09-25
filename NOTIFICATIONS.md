# 收录通知模板 · Notification Templates

> 用途：Awesome YuE 收录新项目后，到对方仓库开一个友好通知 issue。
> 说明：已使用 GitHub PAT 通过 API 代发，**53 个收录仓库全部处理完毕**（2026-09-26）：49 个仓库通知 issue 已发送，4 个仓库（ianiv/YuE2、alisson-anjos/YuE-exllamav2-UI、alisson-anjos/YuE-Interface、WrongProtocol/YuE-exllamav2-UI）关闭了 Issue 区，无法发送——后续可改为关注其 Releases/动态或跳过。
> 原则：只发一条、语气客气、明确给出"调整/下架"出口与联系方式（liuang0307@foxmail.com）。

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

If you'd like the description adjusted, moved to another category, or removed entirely, just reply here or email **liuang0307@foxmail.com** — no questions asked.

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

如果希望修改描述、调整分类或**下架**，直接在本 issue 回复，或发邮件到 **liuang0307@foxmail.com**，我们会尽快处理。

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

---

## 反向链接请求 Backlink Requests（2026-09-26 完成）

> 在上一步的通知 issue 里各追加了**一条**"可选 backlink 请求"评论——请对方在其 README 加一行 `Listed in [awesome-YuE](https://github.com/RevolutionLA/awesome-YuE)`。语气明确 optional，一次性，不刷屏。
> 实现方式：逐一反查每个收录仓库中由 `RevolutionLA` 创建、标题含 `awesome-YuE` 的**未关闭** issue，仅在其上追加评论（已存在同款评论的自动跳过）。

**成功发送 57 条**（仓库#issue 编号）：

```
Blizaine/Maestro#154            CodeCat04/Whiskerwave-Studio#1       Cognito-Inc-451/Yue2-CUDA-Windows#1
DocShotgun/ds-yue-webui#1       EmeraldApple-AI/ComfyUI-YuE2#2        John-yg-Yim/LastAlbum-music-api#1
Joker56156/tio-music-studio#1   KytraScript/ComfyUI-FS_Audio_Suite#3  Ladypoly/YuE2_WebUI#5
LeeAeron/YuE2UI#1               Mozer/YuE-extend#4                    PasiKoodaa/YuE2-Radio#1
Rdx-ai-art/yue2-mlx.pinokio#3   ScryptHunter/ComfyUI-YuE2#6           ServeurpersoCom/yue2.cpp#11
Sparaa/yue2-sidecar#1           Starnodes2024/ComfyUI-YuE2-Trainer#3  T8mars/Comfyui-YuE2-T8#17
TheLocalLab/ComfyUI-SongScribe#1 UnlimitedEditing/ComfyUI-YuE2Fast#1  VincentGourbin/yue2-mlx-swift#2
ace-step/ACE-Step#425           aidec/YuE-exllamav2-GUI-easy#1        arinltte/YuE2Mac#1
arthurfarache/muvflow-yue#1     cicalooo/ComfyUI-YuE2-LongSong#1      daig/yue2-mlx#1
deadjoe/yue2_groove#13          engival/yue2.cpp#1                    filliptm/ComfyUI-FL-YuE2#9
giapnguyen74/yue2-server#1      inikolax/remiqora#8                   krakenunbound/yue2-studio#3
lee101/yue-cog#1                mikkel/yue2-concept-sliders#1         mitnits/yue2-same-music-new-lyrics#1
nheegen/yue2-session-bridge#1   nvmax/ComfyUI-YuE2#3                  o-l-l-i/ComfyUI-Olm-YuE2#3
piscesbody/ComfyUI-YuE2#3       pytraveler/YuE2-ComfyUI#7             sdbds/YuE-for-windows#3
siliconsense/yue2-studio-pc#1   smittyPNW/YuE-Studio#2                sruckh/Yue2-runpod#2
stavitian/yue2-studio#1         tonywestonuk/YuE-Studio#6             usamireko/YuE-exllamav2-Colab#1
vanch007/mlx-Yue#1              vrgamegirl19/Yue2_Studio#20           yolanother/runpod-yuegp-serverless#1
deepbeepmeep/YuEGP#65           joeljuvel/YuE-UI#22                   sgsdxzy/YuE-exllamav2#25
smthemex/ComfyUI_YuE#36         timoncool/YuE2-Studio#6               NoizAI/YuE2-Turbo#1
```

**跳过：**

| 仓库 | 原因 |
|---|---|
| ianiv/YuE2、alisson-anjos/YuE-exllamav2-UI、alisson-anjos/YuE-Interface、WrongProtocol/YuE-exllamav2-UI | 关闭了 Issue 区，无法触达 |
| dynamohum/YuE2gen-studio、deadjoe/yue2-groove-pinokio | 无 open 通知 issue |
| multimodal-art-projection/YuE | 走 PR 通道（见 PROMOTION.md §2.1） |
| deepseek-ai/awesome-deepseek-integration、sindresorhus/awesome、nomadkaraoke/python-audio-separator | README 中的纯参考链接，非收录通知对象 |
| RevolutionLA/YuE2-Music-Workbench | 自有项目 |

**实现踩坑（勿重犯）：**
1. **GitHub 的 issues API 会把 PR 也算作 issue**。首次运行时不慎给官方 PR #203 也发了一条，已删除。需按 `pull_request` 字段或标题排除。
2. **反查通知 issue 必须按 `state=open` 过滤**。早期为若干仓库误开过"重复通知 issue"并自行关闭，若不加状态过滤，`next()` 会选中那条已关闭的重复 issue，从而漏掉真正该评论的原始 issue（YuEGP / YuE-UI / sgsdxzy / smthemex / timoncool 就因此被漏掉，后已补发）。
