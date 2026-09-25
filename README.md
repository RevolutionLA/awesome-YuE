<div align="center">

# 🎵 Awesome YuE

**YuE 生态精选 · 集成、工具、界面、模型、教程与最佳实践**

*A curated list of YuE ecosystem resources: integrations, tools, UIs, models, tutorials and best practices.*

[![GitHub Repo stars](https://img.shields.io/github/stars/RevolutionLA/awesome-YuE?style=social)](https://github.com/RevolutionLA/awesome-YuE/stargazers)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Powered by YuE](https://img.shields.io/badge/Powered%20by-YuE-8A2BE2)](https://github.com/multimodal-art-projection/YuE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**中文为主 · English secondary**（本清单以中文撰写，项目说明辅以英文原名）

</div>

---

YuE（乐）是 [m-a-p](https://github.com/multimodal-art-projection) 团队开源的全曲音乐生成基础模型（lyrics2song），可以只凭歌词与风格提示生成几分钟长的完整歌曲（人声 + 伴奏），被视为开源版 Suno。自 2025 年 1 月发布以来，社区涌现了大量界面、量化加速、ComfyUI 节点、本地移植与音乐制作工作流。本仓库旨在把 **YuE / YuE2 生态**的优秀项目、集成与最佳实践收录成一份持续维护的中文优先清单。

YuE (乐) is an open-source full-song music generation foundation model by the [m-a-p](https://github.com/multimodal-art-projection) team (lyrics2song) — often called "open-source Suno". Since its release in January 2025 the community has built a rich ecosystem of UIs, quantized runtimes, ComfyUI nodes, local ports and music-production workflows. This repo curates the best of the **YuE / YuE2 ecosystem**.

> 📌 收录标准与提交方式见 [贡献指南](CONTRIBUTING.md)。分类排序大致按热度/活跃度，仅供浏览参考。
> 📌 See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria. Categories are loosely ordered by popularity/activity.

---

## ⭐ 特别推荐 Featured

<div align="center">

### 🎹 [YuE2-Music-Workbench](https://github.com/RevolutionLA/YuE2-Music-Workbench)

**本地 AI 音乐生成工作站 · Local Offline AI Music Workstation**

YuE2 写歌 + AI 翻唱 + RVC 换声 + LRC 滚动歌词 + 批量队列，100% 离线开箱即用，一个免费的本地 Suno 替代方案。
YuE2 songwriting + AI covers + RVC voice conversion + LRC synced lyrics + batch queue — fully offline, a free local Suno alternative.

`Windows` · `Python` · `gguf/llama-cpp` · `RVC` · `lyrics2song`

</div>

---

## 📑 目录

- [官方资源 Official](#官方资源-official)
- [图形界面 GUI](#图形界面-gui)
- [量化与推理加速 Quantization & Acceleration](#量化与推理加速-quantization--acceleration)
- [Apple Silicon / 本地移植 Local Ports](#apple-silicon--本地移植-local-ports)
- [ComfyUI 集成 ComfyUI Integrations](#comfyui-集成-comfyui-integrations)
- [音乐制作工具链 Music Production Toolchain](#音乐制作工具链-music-production-toolchain)
- [云部署与服务化 Cloud & Serving](#云部署与服务化-cloud--serving)
- [平台适配 Windows / Linux](#平台适配-windows--linux)
- [教程与最佳实践 Tutorials & Best Practices](#教程与最佳实践-tutorials--best-practices)
- [相关项目 Related Projects](#相关项目-related-projects)
- [社区 Community](#社区-community)
- [贡献 Contributing](#贡献-contributing)

---

## 🏛️ 官资源 Official

<!-- markdownlint-disable MD034 -->

| 项目 | 说明 | 备注 |
|---|---|---|
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | YuE / YuE2 官方仓库。YuE2 引入符号规划（ABC 可编辑乐谱）、零样本翻唱与 agentic 音乐编辑，质量对标 Suno v5 | Apache-2.0 |
| [YuE2 官网](https://map-yue2.github.io/) | YuE2 项目主页，含在线试听 Demo | — |
| [YuE1 Demo 页](https://map-yue.github.io/) | YuE 首代模型演示页 | — |
| [arXiv:2503.08638](https://arxiv.org/abs/2503.08638) | 论文《YuE: Scaling Open Foundation Models for Long-Form Music Generation》 | 2025.03 |
| [m-a-p on Hugging Face](https://huggingface.co/m-a-p) | 全部官方权重：YuE-s1-7B（en/zh/jp-kr × cot/icl）、YuE-s2-1B、YuE2-3B、YuE2-Vae、YuE-upsampler 等 | — |
| [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | ComfyUI 官方合作的一体化 checkpoint（`yue2_3b_bf16.safetensors`，约 7.8 GB） | ComfyUI 专用 |
| [官方文档 docs/generation.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/generation.md) | YuE2 生成指南：`SongRequest` / `GenerationConfig` / 符号乐谱编辑 / 产物与可复现性 | — |
| [官方内置 Skill：yue2-music](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) | 官方随仓库提供的 Agent Skill（含 ABC 编辑参考与 `run_yue2.py` 脚本） | — |

> **YuE2 架构速览**：2.2B AR 语言模型负责歌曲规划与语义 token（`full`/`melody`/`off` 三种 CoT 模式）→ 1.5B NAR flow-matching 分支生成 64 通道 VAE latent → 48 kHz 立体声 VAE 解码输出；支持 vLLM 加速、CUDA Graph、权重 offload。

## 🖥️ 图形界面 GUI

> 图形界面，一键/低门槛出歌。

| 项目 | 说明 | 平台 | 备注 |
|---|---|---|---|
| [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) | 本地 AI 歌曲生成器，带可编辑乐谱（五线谱） | Windows/Linux | MIT |
| [deepbeepmeep/YuEGP](https://github.com/deepbeepmeep/YuEGP) | YuEGP：专为"显卡穷人"优化（GPU Poor），MMGP 显存管理 | Linux/Win | YuE 官方 README 推荐 |
| [joeljuvel/YuE-UI](https://github.com/joeljuvel/YuE-UI) | Gradio 界面：批量生成、时间线可视化、增量续写、会话保存/加载，8GB 显存可跑（量化模型） | 跨平台 | YuE 官方 README 推荐 |
| [sgsdxzy/YuE-exllamav2](https://github.com/sgsdxzy/YuE-exllamav2) | ExLlamaV2 加速实现（含 GUI），YuE1 时代最高效的推理方案之一 | Linux/Win | Apache-2.0 |
| [alisson-anjos/YuE-exllamav2-UI](https://github.com/alisson-anjos/YuE-exllamav2-UI) | 基于 YuE-exllamav2 的 Gradio UI，RTX 4090 实测端到端 5.45× 提速；提供 Docker 镜像 | Linux/Win/Docker | Apache-2.0 |
| [vrgamegirl19/Yue2_Studio](https://github.com/vrgamegirl19/Yue2_Studio) | YuE2 桌面音乐工作室 | Windows | Apache-2.0 |
| [krakenunbound/yue2-studio](https://github.com/krakenunbound/yue2-studio) | 原生 Windows 音乐工作室：本地模型下载、歌词/封面编辑 | Windows | — |
| [Ladypoly/YuE2_WebUI](https://github.com/Ladypoly/YuE2_WebUI) | YuE2 WebUI | — | Apache-2.0 |
| [dynamohum/YuE2gen-studio](https://github.com/dynamohum/YuE2gen-studio) | 翻唱录音 / 提示词写歌 / 编辑的 Web 界面 | — | Apache-2.0 |
| [Mozer/YuE-extend](https://github.com/Mozer/YuE-extend) | YuE1 音乐续写（mp3 extend）+ GUI，另有 Colab 版 | 跨平台 | Apache-2.0 |
| [CodeCat04/Whiskerwave-Studio](https://github.com/CodeCat04/Whiskerwave-Studio) | 本地优先的 YuE2 生成 GUI + Ollama 辅助作词 | — | — |
| [DocShotgun/ds-yue-webui](https://github.com/DocShotgun/ds-yue-webui) | YuE2 WebUI：生成 / 翻唱 / 编辑 | — | — |
| [aidec/YuE-exllamav2-GUI-easy](https://github.com/aidec/YuE-exllamav2-GUI-easy) | YuE-exllamav2 简易版 GUI（繁体中文界面） | Windows | — |
| [LeeAeron/YuE2UI](https://github.com/LeeAeron/YuE2UI) | YuE2 桌面应用 | — | Apache-2.0 |

## ⚡ 量化与推理加速 Quantization & Acceleration

> 显存不足时的量化方案与吞吐优化。

| 项目 | 说明 | 备注 |
|---|---|---|
| [NoizAI/YuE2-Turbo](https://github.com/NoizAI/YuE2-Turbo) | YuE2 高并发推理：同模型同配方，单首 1.68× 提速、并发 3.31× 提升 | Apache-2.0 |
| [Alissonerdx exl2 量化权重](https://huggingface.co/collections/Alissonerdx/yue-models-exllamav2-67a539be76b5225ebda95323) | YuE-s1-7B 的 ExLlamaV2 全系列量化（3.0–8.0 bpw） | HF Collection |
| [Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2](https://huggingface.co/Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2) | exl2 量化权重（Q8/Q6 等） | HF |
| [Alissonerdx/YuE-s1-7B-anneal-en-cot-int8](https://huggingface.co/Alissonerdx/YuE-s1-7B-anneal-en-cot-int8) | bitsandbytes INT8 量化权重 | HF |
| [ServeurpersoCom/yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp) | GGML C++17 便携实现：文本+歌词进，48kHz 立体声出 | MIT |
| [engival/yue2.cpp](https://github.com/engival/yue2.cpp) | YuE2 的 ggml/Vulkan 实现：单个 C++ 可执行文件，无需 Python | MIT |

## 🍎 Apple Silicon / 本地移植 Local Ports

> Mac（MLX / Core ML）与移动端原生运行。

| 项目 | 说明 | 备注 |
|---|---|---|
| [tonywestonuk/YuE-Studio](https://github.com/tonywestonuk/YuE-Studio) | 原生 Mac 应用，面向 Apple Silicon（GPU + Neural Engine）调优 | Apache-2.0 |
| [vanch007/mlx-Yue](https://github.com/vanch007/mlx-Yue) | YuE2-3B 的 Apple Silicon MLX 原生移植（含音频转写） | Apache-2.0 |
| [ianiv/YuE2](https://github.com/ianiv/YuE2) | YuE2 Studio：Apple Silicon（MLX）上的本地 Web 应用 | MIT |
| [VincentGourbin/yue2-mlx-swift](https://github.com/VincentGourbin/yue2-mlx-swift) | Swift/MLX 移植：歌词+风格 → 完整歌曲 | MIT |
| [daig/yue2-mlx](https://github.com/daig/yue2-mlx) | BF16 优先的 MLX/MPS 实验，自动跟随上游 | Apache-2.0 |
| [arinltte/YuE2Mac](https://github.com/arinltte/YuE2Mac) | 本地 AI 歌曲创作工作室（Mac） | MIT |
| [smittyPNW/YuE-Studio](https://github.com/smittyPNW/YuE-Studio) | Apple Silicon 本地创作/编辑/母带，全质量 YuE2 生成与可逆音频处理 | Apache-2.0 |
| [stavitian/yue2-studio](https://github.com/stavitian/yue2-studio) | macOS 应用 + 安装器：YuE2-3B 生成/翻唱/转写 | — |

## 🧩 ComfyUI 集成 ComfyUI Integrations

> ComfyUI 已原生支持 YuE2（PR #16250，`yue2` 分支），以下为社区节点包与相关工作流。

| 项目 | 说明 | 备注 |
|---|---|---|
| ComfyUI 原生支持 | ComfyUI 核心内置 `YuE2GenerateABC` / `YuE2GenerateMusic` 等节点（`comfy_extras/nodes_yue2.py`），使用 [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) 一体化 checkpoint | 官方原生 |
| [smthemex/ComfyUI_YuE](https://github.com/smthemex/ComfyUI_YuE) | YuE1 时代社区最流行的 ComfyUI 节点（Stage A/B 加载器，支持 exl2/INT8 量化） | Apache-2.0 |
| [filliptm/ComfyUI-FL-YuE2](https://github.com/filliptm/ComfyUI-FL-YuE2) | YuE2 音乐生成 + 可编辑钢琴卷帘（piano roll） | Apache-2.0 |
| [T8mars/Comfyui-YuE2-T8](https://github.com/T8mars/Comfyui-YuE2-T8) | YuE2 ComfyUI 节点包 | — |
| [Starnodes2024/ComfyUI-YuE2-Trainer](https://github.com/Starnodes2024/ComfyUI-YuE2-Trainer) | YuE2 LoRA 训练器：用自己的音轨训练风格 LoRA（NAR 分支，24GB 显存推荐），ComfyUI 原生格式输出 | — |
| [ScryptHunter/ComfyUI-YuE2](https://github.com/ScryptHunter/ComfyUI-YuE2) | 依赖隔离的兼容性 fork，适配新版 ComfyUI 与 Transformers | Apache-2.0 |
| [pytraveler/YuE2-ComfyUI](https://github.com/pytraveler/YuE2-ComfyUI) | YuE2-3B 的 ComfyUI 个人适配版 | Apache-2.0 |
| [KytraScript/ComfyUI-FS_Audio_Suite](https://github.com/KytraScript/ComfyUI-FS_Audio_Suite) | 模块化 YuE2 音频生成节点 + 母带/降噪工作流（含封面生成） | — |
| [o-l-l-i/ComfyUI-Olm-YuE2](https://github.com/o-l-l-i/ComfyUI-Olm-YuE2) | 风格+歌词生成歌曲，可选乐谱查看/编辑 | — |
| [nvmax/ComfyUI-YuE2](https://github.com/nvmax/ComfyUI-YuE2) | YuE2 ComfyUI 节点 | Apache-2.0 |
| [piscesbody/ComfyUI-YuE2](https://github.com/piscesbody/ComfyUI-YuE2) | YuE2 ComfyUI 节点（ScryptHunter fork 的上游） | Apache-2.0 |
| [EmeraldApple-AI/ComfyUI-YuE2](https://github.com/EmeraldApple-AI/ComfyUI-YuE2) | YuE2-3B lyrics-to-song 自定义节点 | — |
| [TheLocalLab/ComfyUI-SongScribe](https://github.com/TheLocalLab/ComfyUI-SongScribe) | AI 音乐提示词节点：73 种风格预设 + 歌曲分析（支持 YuE2） | MIT |
| [UnlimitedEditing/ComfyUI-YuE2Fast](https://github.com/UnlimitedEditing/ComfyUI-YuE2Fast) | 运行官方 YuE2 runtime 的快速节点（CUDA Graph 解码） | — |
| [cicalooo/ComfyUI-YuE2-LongSong](https://github.com/cicalooo/ComfyUI-YuE2-LongSong) | YuE2 长歌曲生成工作流 | MIT |
| [mitnits/yue2-same-music-new-lyrics](https://github.com/mitnits/yue2-same-music-new-lyrics) | 保留旋律、改唱新歌词：Gradio UI + ComfyUI 节点（YuE2 + SheetSage2） | Apache-2.0 |

## 🎛️ 音乐制作工具链 Music Production Toolchain

> 把 YuE2 接入 DAW、乐谱编辑与音频后期。

| 项目 | 说明 | 备注 |
|---|---|---|
| [mikkel/yue2-concept-sliders](https://github.com/mikkel/yue2-concept-sliders) | 16 个 YuE2 音乐概念滑杆（Concept Sliders），支持 ComfyUI | MIT |
| [nheegen/yue2-session-bridge](https://github.com/nheegen/yue2-session-bridge) | Ableton Max for Live 设备：Session MIDI 和声 → ABC → YuE2 | MIT |
| [o-l-l-i 系工作流](https://github.com/o-l-l-i/ComfyUI-Olm-YuE2) | 乐谱查看/编辑 + 翻唱模式的完整 ComfyUI 工作流示例 | — |

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

## 🪟 平台适配 Windows / Linux

| 项目 | 说明 | 备注 |
|---|---|---|
| [sdbds/YuE-for-windows](https://github.com/sdbds/YuE-for-windows) | YuE1 Windows 原生支持（Gradio + Docker） | Apache-2.0 |
| [Cognito-Inc-451/Yue2-CUDA-Windows](https://github.com/Cognito-Inc-451/Yue2-CUDA-Windows) | YuE2 CUDA Windows 适配 | — |
| [siliconsense/yue2-studio-pc](https://github.com/siliconsense/yue2-studio-pc) | 一键批处理在 NVIDIA 显卡上运行 YuE2（生歌 + 翻唱） | — |
| [Rdx-ai-art/yue2-mlx.pinokio](https://github.com/Rdx-ai-art/yue2-mlx.pinokio) | YuE2-3B 的 Pinokio 一键安装包（Mac MLX） | — |
| [deadjoe/yue2_groove](https://github.com/deadjoe/yue2_groove) | 非官方 YuE2 Web UI（Apple Silicon 优先，Linux/CUDA 可用），另有 [Pinokio 版](https://github.com/deadjoe/yue2-groove-pinokio) | Apache-2.0 |
| [PasiKoodaa/YuE2-Radio](https://github.com/PasiKoodaa/YuE2-Radio) | 本地 AI 电台（YuE2 持续播放） | MIT |
| [Joker56156/tio-music-studio](https://github.com/Joker56156/tio-music-studio) | 本地 AI 音乐工作室：ACE-Step 1.5 / YuE / DiffRhythm 集成 | — |

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
- **ComfyUI Wiki：YuE2-3B 介绍与原生支持**：[comfyui-wiki.com/en/news/2026-09-11-yue2-3b](https://comfyui-wiki.com/en/news/2026-09-11-yue2-3b) — 含 ComfyUI 依赖冲突（PyTorch/Transformers 版本 pin）注意事项。
- **DeepWiki：YuE 代码解读**：[deepwiki.com/multimodal-art-projection/YuE](https://deepwiki.com/multimodal-art-projection/YuE) — `YuE2Pipeline` 架构、AR/NAR/VAE 模块与后端加速的可视化文档。
- **显存速查（社区经验）**：24GB+ → 官方 BF16；16GB → exl2/INT8 量化；8GB → YuE-UI 量化模式 / YuEGP MMGP；Mac → MLX 移植。

## 🔗 相关项目 Related Projects

| 项目 | 说明 |
|---|---|
| [ace-step/ACE-Step](https://github.com/ace-step/ACE-Step) | 另一个开源音乐生成基础模型，常与 YuE2 对比/搭配（remiqora 把两者集成在同一界面） |
| [inikolax/remiqora](https://github.com/inikolax/remiqora) | 统一 ACE-Step 1.5 与 YuE2-3B 的本地 AI 音乐工作室（Vue） | 
| [m-a-p/MERT](https://huggingface.co/m-a-p/MERT-v1-95M) | YuE2 评测所用音乐理解模型（MERT2） |
| [SheetSage2](https://huggingface.co/m-a-p) | YuE2 评测所用歌词对齐乐谱模型 |

## 👥 社区 Community

- [GitHub Issues / Discussions](https://github.com/multimodal-art-projection/YuE/issues) — 官方仓库问题与路线图（vLLM/sglang、llama.cpp、stemgen 等）。
- [Hugging Face m-a-p 组织](https://huggingface.co/m-a-p) — 权重发布与模型卡。
- [map-yue2.github.io](https://map-yue2.github.io/) — 在线试听 Demo。

## 🤝 贡献 Contributing

欢迎提交 PR！收录标准、格式规范与提交步骤请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。中英文说明均可，中文优先。

## ⚖️ 许可 License

本清单以 [CC0 1.0](LICENSE) 发布。所收录项目各自遵循其许可证，使用前请查阅各项目主页。

---

<div align="center">

**[⬆ 回到顶部](#-awesome-yue)**

Made with ❤️ by the YuE community · Inspired by [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) & [sindresorhus/awesome](https://github.com/sindresorhus/awesome)

</div>

