<div align="center">

# 🎵 Awesome YuE

**YuE 生态精选 · 集成、工具、界面、模型、教程与最佳实践**

*A curated list of YuE ecosystem resources: integrations, tools, UIs, models, tutorials and best practices.*

[![GitHub Repo stars](https://img.shields.io/github/stars/RevolutionLA/awesome-YuE?style=social)](https://github.com/RevolutionLA/awesome-YuE/stargazers)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Powered by YuE](https://img.shields.io/badge/Powered%20by-YuE-8A2BE2)](https://github.com/multimodal-art-projection/YuE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

简体中文 | [English](README_EN.md)

</div>

---

YuE（乐）是 [m-a-p](https://github.com/multimodal-art-projection) 团队开源的全曲音乐生成基础模型（lyrics2song），可以只凭歌词与风格提示生成几分钟长的完整歌曲（人声 + 伴奏），被视为开源版 Suno。自 2025 年 1 月发布以来，社区涌现了大量界面、量化加速、ComfyUI 节点、本地移植与音乐制作工作流。2026 年 9 月发布的 YuE2 进一步引入符号规划（可编辑 ABC 乐谱）、零样本翻唱、纯音乐生成与 agentic 音乐编辑，生态也随之扩展到 GGUF/C++ 运行时、LoRA 训练、DAW 集成与移动端。本仓库旨在把 **YuE / YuE2 生态**的优秀项目、集成与最佳实践收录成一份持续维护的中文优先清单。

YuE (乐) is an open-source full-song music generation foundation model by the [m-a-p](https://github.com/multimodal-art-projection) team (lyrics2song) — often called "open-source Suno". Since its release in January 2025 the community has built a rich ecosystem of UIs, quantized runtimes, ComfyUI nodes, local ports and music-production workflows. YuE2 (September 2026) adds symbolic planning with editable ABC scores, zero-shot covers, instrumental generation and agentic music editing; the ecosystem now spans GGUF/C++ runtimes, LoRA training, DAW integration and mobile. This repo curates the best of the **YuE / YuE2 ecosystem**.

> 📊 **收录 95+ 个项目** · 最近更新 2026-10-21 · 每季度巡检链接有效性
> 📌 收录标准与提交方式见 [贡献指南](CONTRIBUTING.md)。分类排序大致按热度/活跃度，仅供浏览参考。
> 📌 See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria. Categories are loosely ordered by popularity/activity.

---

## 📑 目录

- [快速选择 Quick Picks](#-快速选择-quick-picks)
- [官方资源 Official](#️-官方资源-official)
- [图形界面 GUI](#️-图形界面-gui)
- [量化与推理加速 Quantization & Acceleration](#-量化与推理加速-quantization--acceleration)
- [平台适配与本地移植 Platform and Local Ports](#-平台适配与本地移植-platform-and-local-ports)
- [ComfyUI 集成 ComfyUI Integrations](#-comfyui-集成-comfyui-integrations)
- [微调与 LoRA Fine-tuning & LoRA](#️-微调与-lora-fine-tuning--lora)
- [音乐制作工具链 Music Production Toolchain](#️-音乐制作工具链-music-production-toolchain)
- [云部署与服务化 Cloud & Serving](#️-云部署与服务化-cloud--serving)
- [教程与最佳实践 Tutorials & Best Practices](#-教程与最佳实践-tutorials--best-practices)
- [相关项目 Related Projects](#-相关项目-related-projects)
- [社区 Community](#-社区-community)
- [贡献 Contributing](#-贡献-contributing)

---

## 🚀 快速选择 Quick Picks

> 不知道从哪儿开始？按你的硬件和需求直接对号入座，一行搞定。

| 你的情况 | 直接去 |
|---|---|
| 只想先听听效果 | [NOIZ 在线 Demo](https://yue.noizai.net/) — 浏览器免费试玩，不用装环境 |
| Windows，想开箱即用、100% 离线 | [RevolutionLA/YuE2-Music-Workbench](https://github.com/RevolutionLA/YuE2-Music-Workbench) — 写歌 + 翻唱 + RVC 换声 + LRC 歌词 + 批量队列 |
| 想做纯音乐 / 伴奏 | [官方 yue2-music Skill v1.2.0](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) — 新增纯音乐生成与纯音乐翻唱；[timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) 的 Instrumental 开关也可一键去人声 |
| 想翻唱 / 保留旋律换歌词 | [官方 Cover 指南](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) + [SheetSage2](https://huggingface.co/m-a-p/SheetSage2) 扒谱；或 [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio)、[yeufonic](https://github.com/yeufonic/yeufonic) |
| 显存 24GB+，要最好音质 | [官方 YuE2 BF16](https://github.com/multimodal-art-projection/YuE) + [官方 Skill](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) |
| 显存 12–16GB | [YuE2 Q8 GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF)（audio.cpp）或 [Serveurperso Q8 套件](https://huggingface.co/Serveurperso/YuE2-GGUF)（yue2.cpp） |
| 显存 8GB | [YuE2 Q4/Q8 GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) + [audio.cpp](https://github.com/0xShug0/audio.cpp) / [yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp)；社区实测 8–9GB 可出歌 |
| 只有 8GB，且只想跑 YuE1 | [deepbeepmeep/YuEGP](https://github.com/deepbeepmeep/YuEGP) 或 [joeljuvel/YuE-UI](https://github.com/joeljuvel/YuE-UI)（仅 YuE1，不能加载 YuE2） |
| Mac（Apple Silicon） | [vanch007/mlx-Yue](https://github.com/vanch007/mlx-Yue) 或 [arinltte/YuE2Mac](https://github.com/arinltte/YuE2Mac)；也可走 [audio.cpp](https://github.com/0xShug0/audio.cpp) Metal |
| iPhone 上直接出歌（不连服务器） | [PocketAnthem](https://apps.apple.com/us/app/pocketanthem/id6815755463) — App Store 应用，YuE2-3B 经 MLX 全程跑在手机本地 |
| Android 上直接出歌 | [Killa YuE](https://github.com/JackKnifeAI/killa-yue) — 手机本地 YuE2（实验性，Snapdragon GPU / CPU） |
| 想在 ComfyUI 里用 | ComfyUI 原生 `YuE2GenerateMusic` 节点 + [官方工作流模板](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_yue2_text2music.json)，见 [ComfyUI 集成](#-comfyui-集成-comfyui-integrations) |
| 想改乐谱 / 保留旋律换歌词 | [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio)（五线谱）· [FL-YuE2](https://github.com/filliptm/ComfyUI-FL-YuE2)（钢琴卷帘） |
| 要跑云端 / 需要 API | [sruckh/Yue2-runpod](https://github.com/sruckh/Yue2-runpod) · [yue2-sidecar](https://github.com/Sparaa/yue2-sidecar)（FastAPI） |
| 不想装 Python 环境 | [audio.cpp](https://github.com/0xShug0/audio.cpp) 或 [yue2.cpp](https://github.com/engival/yue2.cpp) — C++ 运行时 + GGUF，无需 Python |

> 显存不够？直接翻到 [量化与推理加速](#-量化与推理加速-quantization--acceleration)；想系统了解写法，看 [教程与最佳实践](#-教程与最佳实践-tutorials--best-practices)。

---

## 🏛️ 官方资源 Official

<!-- markdownlint-disable MD034 -->

| 项目 | 说明 | 备注 |
|---|---|---|
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | YuE / YuE2 官方仓库。YuE2 引入符号规划（ABC 可编辑乐谱）、零样本翻唱与 agentic 音乐编辑，质量对标 Suno v5/v6 | 代码 Apache-2.0；权重 CC BY-NC 4.0 |
| [YuE2 官网](https://map-yue2.github.io/) | YuE2 项目主页，含在线试听 Demo | — |
| [NOIZ 在线 Demo](https://yue.noizai.net/) | 浏览器免费试玩 YuE2，无需安装（官方 README 推荐） | 在线服务 |
| [Blizaine/Maestro](https://github.com/Blizaine/Maestro) | 本地歌曲生成/作曲规划/翻唱，内置 YuE2（官方 README 推荐） | — |
| [YuE1 Demo 页](https://map-yue.github.io/) | YuE 首代模型演示页 | — |
| [YuE-v1 分支](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1) | 初代 YuE 的代码、文档与许可；YuE1 工具仍以该分支为准 | Legacy |
| [arXiv:2609.33757](https://arxiv.org/abs/2609.33757) | **YuE2 技术报告**：符号规划、零样本翻唱、agentic 编辑，含自动/专家听测与 WildSongBench 评测 | 2026.09 |
| [arXiv:2610.05336](https://arxiv.org/abs/2610.05336) | **SheetSage2 论文**：音频 → 主旋律乐谱（ABC/MIDI），翻唱与乐谱编辑的转写基础 | 2026.10 |
| [arXiv:2503.08638](https://arxiv.org/abs/2503.08638) | 论文《YuE: Scaling Open Foundation Models for Long-Form Music Generation》 | 2025.03 |
| [m-a-p on Hugging Face](https://huggingface.co/m-a-p) | 官方权重与数据：YuE2-3B、YuE2-Vae（含 legacy）、SheetSage2、MERT2、WildSongBench、YuE1 全系 | — |
| [WildSongBench](https://huggingface.co/datasets/m-a-p/WildSongBench) | 官方全曲生成基准：192 条中英提示词（94 中 / 98 英），含评测协议与复现脚本 | CC BY-NC 4.0 |
| [m-a-p/SheetSage2](https://huggingface.co/m-a-p/SheetSage2) | 官方音频转谱模型（MERT2 编码器），输出可编辑 ABC/MIDI；翻唱与乐谱编辑用 | CC BY-NC 4.0 |
| [m-a-p/MERT-v2-FullSong](https://huggingface.co/m-a-p/MERT-v2-FullSong) · [MERT-v2-30s](https://huggingface.co/m-a-p/MERT-v2-30s) | MERT2 音乐理解模型：全曲/30 秒版本，SheetSage2 编码器与 YuE2 评测用 | CC BY-NC 4.0 |
| [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | ComfyUI 官方合作的一体化 checkpoint（`yue2_3b_bf16.safetensors`，约 7.8 GB） | ComfyUI 专用 |
| [官方文档 docs/generation.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/generation.md) | YuE2 生成指南：`SongRequest` / `GenerationConfig` / 符号乐谱编辑 / 产物与可复现性 | — |
| [官方 Cover 指南 docs/covers.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) | SheetSage2 转写参考录音 → ABC 旋律 → `cot="melody"` 换歌词/风格；含完整命令与示例 | — |
| [官方评测协议 docs/benchmarks.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md) | WildSongBench、翻唱与乐谱编辑的评测方法；含 Suno v5/v6 对比与复现说明 | — |
| [官方内置 Skill：yue2-music](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) | Agent Skill **v1.2.0（2026-09-25）**：新增纯音乐生成与纯音乐翻唱，支持 ABC/参考录音；含 `run_yue2.py` 与 instrumental 子技能 | — |

> **许可提醒**：YuE2 的代码、Agent Skill 与文档为 Apache-2.0；模型权重为 **CC BY-NC 4.0**（个人与创作者可免费使用并商业化产出，企业商用权重需联系官方）。

> **YuE2 架构速览**：2.2B AR 语言模型负责歌曲规划与语义 token（`full`/`melody`/`off` 三种 CoT 模式）→ 1.5B NAR flow-matching 分支生成 64 通道 VAE latent → 48 kHz 立体声 VAE 解码输出；支持 vLLM 加速、CUDA Graph、权重 offload。

## 🖥️ 图形界面 GUI

> 图形界面，一键/低门槛出歌。标有 **YuE1** 的条目仅支持初代 YuE；YuE2 用户请优先看前面的 YuE2 应用。

| 项目 | 说明 | 平台 | 备注 |
|---|---|---|---|
| ⭐ [RevolutionLA/YuE2-Music-Workbench](https://github.com/RevolutionLA/YuE2-Music-Workbench) | 本地 AI 音乐生成工作站：YuE2 写歌 + AI 翻唱 + RVC 换声 + LRC 滚动歌词 + 批量队列，100% 离线开箱即用 | Windows | 特别推荐 |
| [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) | 本地 AI 歌曲工作室（v3.7.0）：可编辑五线谱、SheetSage2 翻唱、纯音乐开关、六轨分离、音频转 MIDI 与内置 LoRA 训练 | Windows/Linux | MIT |
| [scragnog/HOT-Step-CPP](https://github.com/scragnog/HOT-Step-CPP) | C++/GGML 桌面音乐工作站：ACE-Step 1.5、MiniMax-Music3、YuE2 三引擎切换；内置数据集标注与原生 AR/NAR LoRA 联合训练，无需 Python | Win/Linux/macOS | MIT |
| [igrbible/Ruach_Studio](https://github.com/igrbible/Ruach_Studio) | 基于 yue2.cpp 的完整 YuE2 工作站：ABC 乐谱编辑、双种子、作品库/收藏、200 种乐器探测、内置 LoRA 训练 | Windows/NVIDIA | AGPL-3.0 |
| [lvxworld/lux-in-music](https://github.com/lvxworld/lux-in-music) | 通过 audio.cpp 在 Apple Silicon 本地出歌：Vibe 风格参考、分轨混音、段落编辑 | macOS Apple Silicon | MIT |
| [yeufonic/yeufonic](https://github.com/yeufonic/yeufonic) | Web 界面 + Docker/Windows 安装器：提示词写歌/录音翻唱、ABC 编辑、分轨、LoRA 训练与导入分享；后端用 ComfyUI + YuE2 节点 | Docker/Win | — |
| [victorcampeanu/OpenSuno-YuE2](https://github.com/victorcampeanu/OpenSuno-YuE2) | Mac/NVIDIA 本地歌曲工作室：Melody/Chords 规划、Composition/Weirdness 等音乐化滑杆、模型编曲、LoRA 目录、从保存 token 重渲染 | macOS/Win | MIT |
| [deepbeepmeep/YuEGP](https://github.com/deepbeepmeep/YuEGP) | YuEGP（YuE1）：专为"显卡穷人"优化（GPU Poor），MMGP 显存管理 | Linux/Win | YuE-v1 README 推荐 |
| [joeljuvel/YuE-UI](https://github.com/joeljuvel/YuE-UI) | YuE-UI（YuE1）：Gradio 界面，批量生成、时间线可视化、增量续写、会话保存/加载，8GB 显存可跑（量化模型） | 跨平台 | YuE-v1 README 推荐 |
| [sgsdxzy/YuE-exllamav2](https://github.com/sgsdxzy/YuE-exllamav2) | ExLlamaV2 加速实现（含 GUI），YuE1 时代最高效的推理方案之一 | Linux/Win | Apache-2.0 |
| [alisson-anjos/YuE-exllamav2-UI](https://github.com/alisson-anjos/YuE-exllamav2-UI) | （YuE1）基于 YuE-exllamav2 的 Gradio UI，RTX 4090 实测端到端 5.45× 提速；提供 Docker 镜像 | Linux/Win/Docker | Apache-2.0 |
| [alisson-anjos/YuE-Interface](https://github.com/alisson-anjos/YuE-Interface) | （YuE1）Docker 化 Gradio 界面，环境变量一键拉取全部官方/量化模型，本地与 RunPod 均可部署 | Docker/RunPod | — |
| [WrongProtocol/YuE-exllamav2-UI](https://github.com/WrongProtocol/YuE-exllamav2-UI) | YuE-exllamav2 的原始 Gradio UI（YuE1；YuE-v1 README 推荐） | Linux/Win | — |
| [vrgamegirl19/Yue2_Studio](https://github.com/vrgamegirl19/Yue2_Studio) | YuE2 桌面音乐工作室 | Windows | Apache-2.0 |
| [krakenunbound/yue2-studio](https://github.com/krakenunbound/yue2-studio) | 原生 Windows 音乐工作室：本地模型下载、歌词/封面编辑 | Windows | — |
| [Ladypoly/YuE2_WebUI](https://github.com/Ladypoly/YuE2_WebUI) | YuE2 WebUI | — | Apache-2.0 |
| [dynamohum/YuE2gen-studio](https://github.com/dynamohum/YuE2gen-studio) | 翻唱录音 / 提示词写歌 / 编辑的 Web 界面 | — | Apache-2.0 |
| [Mozer/YuE-extend](https://github.com/Mozer/YuE-extend) | YuE1 音乐续写（mp3 extend）+ GUI，另有 Colab 版 | 跨平台 | Apache-2.0 |
| [CodeCat04/Whiskerwave-Studio](https://github.com/CodeCat04/Whiskerwave-Studio) | 本地优先的 YuE2 生成 GUI + Ollama 辅助作词 | — | — |
| [DocShotgun/ds-yue-webui](https://github.com/DocShotgun/ds-yue-webui) | YuE2 WebUI：生成 / 翻唱 / 编辑 | — | — |
| [aidec/YuE-exllamav2-GUI-easy](https://github.com/aidec/YuE-exllamav2-GUI-easy) | （YuE1）YuE-exllamav2 简易版 GUI（繁体中文界面） | Windows | — |
| [LeeAeron/YuE2UI](https://github.com/LeeAeron/YuE2UI) | YuE2 桌面应用（深度改版独立开发，暂未公开源码） | Windows 10/11 | Apache-2.0 |

## ⚡ 量化与推理加速 Quantization & Acceleration

> 显存不足时的量化方案与吞吐优化。**YuE2 与 YuE1 权重互不兼容**；标有 YuE1 的条目不能加载 YuE2。

| 项目 | 说明 | 备注 |
|---|---|---|
| [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) | 通用 C++/GGML 音频推理引擎（3.6k★）：YuE2 支持 ABC 规划、AR/NAR LoRA、SheetSage2 转谱；BF16/Q8/Q4，NVIDIA/AMD/Metal/CPU | Apache-2.0 |
| [NoizAI/YuE2-Turbo](https://github.com/NoizAI/YuE2-Turbo) | YuE2 高并发推理与在线服务工具包：同模型同配方，单首 1.68× 提速、并发 3.31× 提升 | Apache-2.0 |
| [audio-cpp/Yue2-3B-GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) | audio.cpp 官方 YuE2 GGUF：BF16/Q8_0/Q4_0 主模型 + F32/F16 VAE + sidecar；含 CLI/WebUI 示例 | CC BY-NC 4.0 |
| [Serveurperso/YuE2-GGUF](https://huggingface.co/Serveurperso/YuE2-GGUF) | yue2.cpp 预量化 GGUF 套件（Q8 3.81 GB + VAE 530 MB，整套约 5.4 GB）；含 MERT2 / SheetSage2 / realaudio tokenizer | CC BY-NC 4.0 |
| [VincentGOURBIN/yue2-mlx-packs](https://huggingface.co/VincentGOURBIN/yue2-mlx-packs) | YuE2-3B 的 MLX 预量化包（int4-mixed-head 2.5 GB / qint8-all-head 3.5 GB / int4-head 4.4 GB），引擎下载时 SHA-256 校验 | CC BY-NC 4.0 |
| [ServeurpersoCom/yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp) | GGML C++17 便携实现 + 浏览器 UI 服务：歌词/风格 → 48kHz 立体声；支持 SheetSage2 扒谱翻唱、AR/NAR LoRA | MIT |
| [engival/yue2.cpp](https://github.com/engival/yue2.cpp) | ggml/Vulkan 实现：v0.1.1 提供 Win/Linux 单文件二进制；EAGLE-3 投机解码、歌词/ABC 文件输入、曲中 context 换 prompt（[演示](https://www.youtube.com/watch?v=gMS2Ko7s97o)） | MIT |
| [WaveCut/YuE2-3B-OrbitQuant-W4A4](https://huggingface.co/WaveCut/YuE2-3B-OrbitQuant-W4A4) | 实验性 W4A4 量化：3.04 GB（较 BF16 -58%），Linux/CUDA，含 RTX 4090 速度/显存基准 | CC BY-NC 4.0 |
| [engival/YuE2-3B-EAGLE3-draft-GGUF](https://huggingface.co/engival/YuE2-3B-EAGLE3-draft-GGUF) | 154 MB EAGLE-3 draft head，配合 yue2.cpp 的投机解码，加速语义 token 阶段 | CC BY-NC 4.0 |
| [Alissonerdx exl2 量化权重](https://huggingface.co/collections/Alissonerdx/yue-models-exllamav2-67a539be76b5225ebda95323) | （YuE1）YuE-s1-7B 的 ExLlamaV2 全系列量化（3.0–8.0 bpw） | HF Collection |
| [Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2](https://huggingface.co/Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2) | （YuE1）exl2 量化权重（Q8/Q6 等） | HF |
| [Alissonerdx/YuE-s1-7B-anneal-en-cot-int8](https://huggingface.co/Alissonerdx/YuE-s1-7B-anneal-en-cot-int8) | （YuE1）bitsandbytes INT8 量化权重 | HF |

## 📦 平台适配与本地移植 Platform and Local Ports

> Mac（MLX / Core ML）、Windows / Linux 与 Android 的原生运行与一键安装，按平台分组。

| 项目 | 说明 | 备注 |
|---|---|---|
| [tonywestonuk/YuE-Studio](https://github.com/tonywestonuk/YuE-Studio) | 原生 Mac 应用，面向 Apple Silicon（GPU + Neural Engine）调优 | Apache-2.0 |
| [vanch007/mlx-Yue](https://github.com/vanch007/mlx-Yue) | YuE2-3B 的 Apple Silicon MLX 原生移植（含音频转写） | Apache-2.0 |
| [ianiv/YuE2](https://github.com/ianiv/YuE2) | YuE2 Studio：Apple Silicon（MLX）上的本地 Web 应用 | MIT |
| [VincentGourbin/yue2-mlx-swift](https://github.com/VincentGourbin/yue2-mlx-swift) | Swift/MLX 移植（Mac + iPhone 全本地）：歌词+风格 → 完整歌曲，App Store 应用 [PocketAnthem](https://apps.apple.com/us/app/pocketanthem/id6815755463) 的引擎，7 个参考量化配置（4bit-tiny 2.6 GB 起） | MIT |
| [daig/yue2-mlx](https://github.com/daig/yue2-mlx) | BF16 优先的 MLX/MPS 实验，自动跟随上游 | Apache-2.0 |
| [arinltte/YuE2Mac](https://github.com/arinltte/YuE2Mac) | macOS 原生歌曲创作工作室：YuE2-3B 本地 MLX 运行，LITE/PRO 双 UI、队列、歌曲库、草稿→成品、可编辑 ABC 乐谱、高级采样、Apple Intelligence 本地 AI 写词 | MIT |
| [stavitian/yue2-studio](https://github.com/stavitian/yue2-studio) | macOS 应用 + 安装器：YuE2-3B 生成/翻唱/转写（含 24GB Mac 修复） | — |
| [sdbds/YuE-for-windows](https://github.com/sdbds/YuE-for-windows) | YuE1 Windows 原生支持（Gradio + Docker） | Apache-2.0 |
| [Cognito-Inc-451/Yue2-CUDA-Windows](https://github.com/Cognito-Inc-451/Yue2-CUDA-Windows) | YuE2 CUDA Windows 适配 | — |
| [siliconsense/yue2-studio-pc](https://github.com/siliconsense/yue2-studio-pc) | 一键批处理在 NVIDIA 显卡上运行 YuE2（生歌 + 翻唱） | — |
| [Rdx-ai-art/yue2-mlx.pinokio](https://github.com/Rdx-ai-art/yue2-mlx.pinokio) | YuE2-3B 的 Pinokio 一键安装包（Mac MLX） | — |
| [deadjoe/yue2_groove](https://github.com/deadjoe/yue2_groove) | 非官方 YuE2 Web UI（Apple Silicon 优先，Linux/CUDA 可用），另有 [Pinokio 版](https://github.com/deadjoe/yue2-groove-pinokio) | Apache-2.0 |
| [PasiKoodaa/YuE2-Radio](https://github.com/PasiKoodaa/YuE2-Radio) | 本地 AI 电台（YuE2 持续播放） | MIT |
| [Joker56156/tio-music-studio](https://github.com/Joker56156/tio-music-studio) | 本地 AI 音乐工作室：ACE-Step 1.5 / YuE / DiffRhythm 集成 | — |
| [JackKnifeAI/killa-yue](https://github.com/JackKnifeAI/killa-yue) | Android 原生 YuE2 工作室（实验性）：手机本地生成（Snapdragon GPU 或 CPU）、分轨、混音、录音；[APK 下载](https://github.com/JackKnifeAI/killa-yue/releases) | Apache-2.0 |

## 🧩 ComfyUI 集成 ComfyUI Integrations

> ComfyUI 已原生支持 YuE2（PR #16250，`yue2` 分支），以下为社区节点包与相关工作流；官方另提供 [text-to-music 工作流模板](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_yue2_text2music.json)。

| 项目 | 说明 | 备注 |
|---|---|---|
| ComfyUI 原生支持 | ComfyUI 核心内置 `YuE2GenerateABC` / `YuE2GenerateMusic` 等节点（`comfy_extras/nodes_yue2.py`），使用 [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) 一体化 checkpoint；2026-09 起加入 CFG 控制与 AMD 修复 | 官方原生 |
| [smthemex/ComfyUI_YuE](https://github.com/smthemex/ComfyUI_YuE) | 已升级支持 YuE2 与 Cover 模式（加载 SheetSage2 + MERT2），同时保留 YuE1 Stage A/B 与 exl2/INT8 量化 | Apache-2.0 |
| [filliptm/ComfyUI-FL-YuE2](https://github.com/filliptm/ComfyUI-FL-YuE2) | YuE2 音乐生成 + 可编辑钢琴卷帘（piano roll） | Apache-2.0 |
| [T8mars/Comfyui-YuE2-T8](https://github.com/T8mars/Comfyui-YuE2-T8) | YuE2 ComfyUI 节点包 | — |
| [ScryptHunter/ComfyUI-YuE2](https://github.com/ScryptHunter/ComfyUI-YuE2) | YuE2 ComfyUI integration with Native/Legacy workflows, ABC editing and duration control, SheetSage2 support, and universal LoRA/LoKr adapters (AR/NAR).（Native/Legacy 工作流、ABC 编辑与时长控制、SheetSage2 支持、通用 LoRA/LoKr 适配器 AR/NAR） | Apache-2.0 |
| [pytraveler/YuE2-ComfyUI](https://github.com/pytraveler/YuE2-ComfyUI) | 钢琴卷帘乐谱编辑 + Edit Track（对成品做重录/剪切/移动/延长）+ 音频或 MIDI 翻唱 + 作词与 LoRA 支持 | Apache-2.0 |
| [KytraScript/ComfyUI-FS_Audio_Suite](https://github.com/KytraScript/ComfyUI-FS_Audio_Suite) | 模块化 YuE2 音频生成节点 + 母带/降噪工作流（含封面生成） | — |
| [o-l-l-i/ComfyUI-Olm-YuE2](https://github.com/o-l-l-i/ComfyUI-Olm-YuE2) | 风格+歌词生成歌曲，可选乐谱查看/编辑 | — |
| [nvmax/ComfyUI-YuE2](https://github.com/nvmax/ComfyUI-YuE2) | YuE2 ComfyUI 节点 | Apache-2.0 |
| [piscesbody/ComfyUI-YuE2](https://github.com/piscesbody/ComfyUI-YuE2) | YuE2 ComfyUI 节点（ScryptHunter fork 的上游） | Apache-2.0 |
| [EmeraldApple-AI/ComfyUI-YuE2](https://github.com/EmeraldApple-AI/ComfyUI-YuE2) | YuE2-3B lyrics-to-song 自定义节点 | — |
| [TheLocalLab/ComfyUI-SongScribe](https://github.com/TheLocalLab/ComfyUI-SongScribe) | AI 音乐提示词节点：73 种风格预设 + 歌曲分析（支持 YuE2） | MIT |
| [UnlimitedEditing/ComfyUI-YuE2Fast](https://github.com/UnlimitedEditing/ComfyUI-YuE2Fast) | 运行官方 YuE2 runtime 的快速节点（CUDA Graph 解码） | — |
| [cicalooo/ComfyUI-YuE2-LongSong](https://github.com/cicalooo/ComfyUI-YuE2-LongSong) | YuE2 长歌曲生成工作流 | MIT |
| [mitnits/yue2-same-music-new-lyrics](https://github.com/mitnits/yue2-same-music-new-lyrics) | 保留旋律、改唱新歌词：Gradio UI + ComfyUI 节点（YuE2 + SheetSage2） | Apache-2.0 |
| [TheAwaken1/ComfyUI-SongLRC](https://github.com/TheAwaken1/ComfyUI-SongLRC) | 把 YuE2 生成结果写成与音频同名的逐行 `.lrc`；可用 ABC 乐谱校正时间轴，兼容 ComfyUI-FL-YuE2 | MIT |

## 🎚️ 微调与 LoRA Fine-tuning & LoRA

> YuE2 的 AR（planner）与 NAR（声学）两半都可训练 LoRA；以下覆盖 ComfyUI 内训练、独立训练基座与社区适配器。timoncool/YuE2-Studio、Ruach_Studio、yeufonic 也内置训练页。

| 项目 | 说明 | 备注 |
|---|---|---|
| [Starnodes2024/ComfyUI-YuE2-Trainer](https://github.com/Starnodes2024/ComfyUI-YuE2-Trainer) | ComfyUI 内训练 YuE2 风格 LoRA（NAR 分支，24GB 显存推荐），输出 ComfyUI 原生格式 | — |
| [speedyrulz/ComfyUI-YuE2-Trainer](https://github.com/speedyrulz/ComfyUI-YuE2-Trainer) | 在 ComfyUI 内分别训练 NAR 声学 MODEL LoRA 与 AR planner CLIP LoRA，可直接给原生 YuE2 节点加载 | Apache-2.0 |
| [Mothersuperior/YuE2-instrumental-cot-full-loras](https://huggingface.co/Mothersuperior/YuE2-instrumental-cot-full-loras) | 纯音乐 AR LoRA（rank 64，2.7k 首器乐 + SheetSage2 ABC 训练），配合 `cot="full"` 生成有段落规划的纯音乐 | CC BY-NC 4.0 |
| [scragnog/YuE2-GGUF](https://huggingface.co/scragnog/YuE2-GGUF) | HOT-Step 联合 AR/NAR 训练用 `int8_convrot` 基座（非推理 GGUF），配套原生 C++ 训练器 | CC BY-NC 4.0 |

## 🎛️ 音乐制作工具链 Music Production Toolchain

> 把 YuE2 接入 DAW、乐谱编辑、哼唱输入与音频后期。

| 项目 | 说明 | 备注 |
|---|---|---|
| [betweentwomidnights/gary4juce](https://github.com/betweentwomidnights/gary4juce) | VST3/AU：把 YuE2（yuey）、MusicGen 等 8 个模型放进 DAW；按 tempo/key 生成、翻唱/续写、ABC 拖成 MIDI、本地分轨 | Windows/macOS · AGPL-3.0 |
| [mikkel/yue2-concept-sliders](https://github.com/mikkel/yue2-concept-sliders) | 16 个 YuE2 音乐概念滑杆（Concept Sliders），支持 ComfyUI | MIT |
| [nheegen/yue2-session-bridge](https://github.com/nheegen/yue2-session-bridge) | Ableton Max for Live 设备：Session MIDI 和声 → ABC → YuE2 | MIT |
| [Mothersuperior/YuE2-hum-to-song](https://huggingface.co/Mothersuperior/YuE2-hum-to-song) · [HF Space](https://huggingface.co/spaces/Mothersuperior/yue2-hum-to-song) | 哼唱 10–30 秒 + 风格/歌词 → 保持旋律的完整歌曲：AR 乐谱续写 + NAR prosody adapter，附 ComfyUI/脚本用法 | CC BY-NC 4.0 |

## ☁️ 云部署与服务化 Cloud & Serving

| 项目 | 说明 | 备注 |
|---|---|---|
| [yolanother/runpod-yuegp-serverless](https://github.com/yolanother/runpod-yuegp-serverless) | RunPod Serverless 上的 YuEGP worker | — |
| [lee101/yue-cog](https://github.com/lee101/yue-cog) | YuE2 的 Cog 打包 + RunPod serverless 适配器 | — |
| [sruckh/Yue2-runpod](https://github.com/sruckh/Yue2-runpod) | YuE2 RunPod Serverless worker（风格+歌词 → 完整歌曲） | — |
| [Sparaa/yue2-sidecar](https://github.com/Sparaa/yue2-sidecar) | FastAPI 任务 API（基于 yue2-infer，支持 ABC 翻唱与长歌） | Apache-2.0 |
| [arthurfarache/muvflow-yue](https://github.com/arthurfarache/muvflow-yue) | YuE 音乐生成 API（SaladCloud） | — |
| [giapnguyen74/yue2-server](https://github.com/giapnguyen74/yue2-server) | YuE2 模型服务器 | — |
| [John-yg-Yim/LastAlbum-music-api](https://github.com/John-yg-Yim/LastAlbum-music-api) | 基于 YuE 的 FastAPI 歌曲生成服务（LastAlbum 后端） | — |
| [usamireko/YuE-exllamav2-Colab](https://github.com/usamireko/YuE-exllamav2-Colab) | Google Colab 一键运行 YuE-exllamav2 | Apache-2.0 |

## 📚 教程与最佳实践 Tutorials & Best Practices

- **官方 Prompt 工程指南**：[genre.txt / lyrics.txt 写法](https://github.com/multimodal-art-projection/YuE#prompt-engineering) — 歌曲分段标签（`[Verse]`/`[Chorus]`）、风格标签顺序等。
- **官方示例工作流视频**：Fahd 的 [YuE 快速上手视频](https://github.com/multimodal-art-projection/YuE#quick-start)。
- **YuE2 提示词结构**：`style` 放流派/乐器/人声/语言/速度，`lyrics` 放带分段标签的歌词；参考 [examples/song.json](https://github.com/multimodal-art-projection/YuE/blob/main/examples/song.json)。
- **ICL 翻唱最佳实践**（官方 README 摘录）：
  1. 双轨 ICL（人声轨 + 伴奏轨）音乐性与提示遵循最好；
  2. 用副歌片段做参考音频效果更佳；
  3. 约 30 秒参考音频为宜；
  4. 可用 [python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) 或 UVR 分离音轨；
  5. 提供参考音频会降低多样性，纯 CoT 模式输出更多样。
- **官方翻唱（Cover）流程**：[docs/covers.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) — SheetSage2 转写参考录音 → 编辑 ABC 旋律 → `cot="melody"` → 新歌词/风格；可先用 `examples/melody.abc` 跑通。
- **官方评测与复现**：[docs/benchmarks.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md) + [WildSongBench](https://huggingface.co/datasets/m-a-p/WildSongBench) — 192 条中英提示词、Suno v5/v6 对比与标准 YuE2 复现步骤。
- **Windows 本地部署（Bilibili + 图文）**：[eogee 视频教程](https://www.bilibili.com/video/BV1esaw62EJx) / [图文版](https://eogee.com/article/148) — 用 ComfyUI 便携整合包在 Windows 跑 YuE2，覆盖 ABC 乐谱编辑与旋律复用。
- **本地部署与乐谱白盒实操**：[阿尔的代码屋](https://blog.algieba12.cn/yue2-local-deployment-and-practice/) — uv + ModelScope 国内加速、SheetSage2 翻唱、生成产物逐层解析。
- **HyperAI 云端 Notebook**：[YuE2-3B 教程](https://next.hyper.ai/cn/notebooks/yue2-3b-frontier-open-music-generation) — 带 Gradio Create/Cover 两个标签页，适合没有本地显卡的用户。
- **ComfyUI Wiki：YuE2-3B 介绍与原生支持**：[comfyui-wiki.com/en/news/2026-09-11-yue2-3b](https://comfyui-wiki.com/en/news/2026-09-11-yue2-3b) — 含 ComfyUI 依赖冲突（PyTorch/Transformers 版本 pin）注意事项。
- **DeepWiki：YuE 代码解读**：[deepwiki.com/multimodal-art-projection/YuE](https://deepwiki.com/multimodal-art-projection/YuE) — `YuE2Pipeline` 架构、AR/NAR/VAE 模块与后端加速的可视化文档。
- **显存速查（YuE2）**：24GB+ → 官方 BF16；12–16GB → Q8 GGUF / FP8；8GB → Q4/Q8 GGUF（audio.cpp / yue2.cpp，社区实测 8–9GB）；Mac → MLX / audio.cpp Metal。YuE1 的 YuEGP / YuE-UI 不能加载 YuE2。

## 🔗 相关项目 Related Projects

| 项目 | 说明 |
|---|---|
| [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | 另一个开源音乐生成基础模型（13.8k★），常与 YuE2 对比/搭配；remiqora、HOT-Step 把两者集成在同一界面 |
| [inikolax/remiqora](https://github.com/inikolax/remiqora) | 统一 ACE-Step 1.5 与 YuE2-3B 的本地工作室（v0.4.1）：YuE2 走 audio.cpp 原生服务，含 Demucs 分轨、多轨编辑器与 LoRA 训练 UI |

## 👥 社区 Community

- [GitHub Issues / Discussions](https://github.com/multimodal-art-projection/YuE/issues) — 官方仓库问题与路线图；近期 PR 聚焦 vLLM V2 sampler、Intel XPU、MPS/Windows CUDA 修复，功能请求集中在多声部/独立歌手、时间签名与逐段人声控制。
- [官方 Discord](https://discord.gg/ssAyWMnMzu) — YuE2 社区讨论与作品分享。
- [Hugging Face m-a-p 组织](https://huggingface.co/m-a-p) — 权重、数据集与模型卡。
- [map-yue2.github.io](https://map-yue2.github.io/) — 在线试听 Demo。
- **里程碑（2026-09）**：YuE2 登 GitHub Trending #1、Hugging Face Text-to-Audio Trending #1（官方 README 徽章）。

## 🤝 贡献 Contributing

欢迎提交 PR！收录标准、格式规范与提交步骤请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。中英文说明均可，中文优先。

## ⚖️ 许可 License

本清单以 [CC0 1.0](LICENSE) 发布。所收录项目各自遵循其许可证，使用前请查阅各项目主页。

---

<div align="center">

**[⬆ 回到顶部](#-awesome-yue)**

Made with ❤️ by the YuE community · Inspired by [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) & [sindresorhus/awesome](https://github.com/sindresorhus/awesome)

</div>

