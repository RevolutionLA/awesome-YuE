<div align="center">

# 🎵 Awesome YuE

**A curated list of YuE ecosystem resources: integrations, tools, UIs, models, tutorials and best practices.**

[![GitHub Repo stars](https://img.shields.io/github/stars/RevolutionLA/awesome-YuE?style=social)](https://github.com/RevolutionLA/awesome-YuE/stargazers)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Powered by YuE](https://img.shields.io/badge/Powered%20by-YuE-8A2BE2)](https://github.com/multimodal-art-projection/YuE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[简体中文](README.md) | English

</div>

---

YuE (乐) is an open-source full-song music generation foundation model by the [m-a-p](https://github.com/multimodal-art-projection) team (lyrics2song) — often called "open-source Suno". Since its release in January 2025 the community has built a rich ecosystem of UIs, quantized runtimes, ComfyUI nodes, local ports and music-production workflows. YuE2 (September 2026) adds symbolic planning with editable ABC scores, zero-shot covers, instrumental generation and agentic music editing; the ecosystem now spans GGUF/C++ runtimes, LoRA training, DAW integration and mobile. This repo curates the best of the **YuE / YuE2 ecosystem**.

> 📊 **99 entries (78 GitHub projects + model weights, tutorials and hosted services)** · Recent changes in [commit history](https://github.com/RevolutionLA/awesome-YuE/commits/main) · Link health guarded by a [weekly automated check](https://github.com/RevolutionLA/awesome-YuE/actions/workflows/link-check.yml)
> 📌 See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria. Categories are loosely ordered by popularity/activity.

---

## 📑 Contents

- [Quick Picks](#-quick-picks)
- [Official Resources](#️-official-resources)
- [GUIs](#-guis)
- [Quantization & Acceleration](#-quantization--acceleration)
- [Platform & Local Ports](#-platform--local-ports)
- [ComfyUI Integrations](#-comfyui-integrations)
- [Fine-tuning & LoRA](#️-fine-tuning--lora)
- [Music Production Toolchain](#️-music-production-toolchain)
- [Cloud & Serving](#️-cloud--serving)
- [Tutorials & Best Practices](#-tutorials--best-practices)
- [Related Projects](#-related-projects)
- [Community](#-community)
- [Contributing](#-contributing)

---

## 🚀 Quick Picks

> Not sure where to start? Match your hardware and goal to a row.

| Your situation | Go to |
|---|---|
| Just want to hear it first | [NOIZ online demo](https://yue.noizai.net/) — free in the browser, no setup |
| Windows, want it working out of the box (100% offline) | [RevolutionLA/YuE2-Music-Workbench](https://github.com/RevolutionLA/YuE2-Music-Workbench) — songwriting + covers + RVC + LRC lyrics + batch queue |
| Want instrumental / backing tracks | [Official yue2-music Skill v1.2.0](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) — new instrumental generation and instrumental covers; [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) also has a one-click Instrumental switch |
| Want a cover / keep the melody, swap lyrics | [Official cover guide](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) + [SheetSage2](https://huggingface.co/m-a-p/SheetSage2); or [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio), [yeufonic](https://github.com/yeufonic/yeufonic) |
| 24GB+ VRAM, best quality | [Official YuE2 BF16](https://github.com/multimodal-art-projection/YuE) + [official Skill](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) |
| 12–16GB VRAM | [YuE2 Q8 GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) (audio.cpp) or [Serveurperso Q8 set](https://huggingface.co/Serveurperso/YuE2-GGUF) (yue2.cpp) |
| 8GB VRAM | [YuE2 Q4/Q8 GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) + [audio.cpp](https://github.com/0xShug0/audio.cpp) / [yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp); community reports 8–9GB is enough |
| 8GB and YuE1 only | [deepbeepmeep/YuEGP](https://github.com/deepbeepmeep/YuEGP) or [joeljuvel/YuE-UI](https://github.com/joeljuvel/YuE-UI) (YuE1 only, cannot load YuE2) |
| Mac (Apple Silicon) | [vanch007/mlx-Yue](https://github.com/vanch007/mlx-Yue) or [arinltte/YuE2Mac](https://github.com/arinltte/YuE2Mac); or [audio.cpp](https://github.com/0xShug0/audio.cpp) Metal |
| iPhone, fully local | [PocketAnthem](https://apps.apple.com/us/app/pocketanthem/id6815755463) — YuE2-3B runs entirely on-device via MLX |
| Android, fully local | [Killa YuE](https://github.com/JackKnifeAI/killa-yue) — YuE2 on a phone (experimental; Snapdragon GPU / CPU) |
| Want to use it in ComfyUI | ComfyUI native `YuE2GenerateMusic` node + [official workflow template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_yue2_text2music.json), see [ComfyUI Integrations](#-comfyui-integrations) |
| Want to edit the score / keep melody, swap lyrics | [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) (staff) · [FL-YuE2](https://github.com/filliptm/ComfyUI-FL-YuE2) (piano roll) |
| Need cloud / an API | [sruckh/Yue2-runpod](https://github.com/sruckh/Yue2-runpod) · [yue2-sidecar](https://github.com/Sparaa/yue2-sidecar) (FastAPI) |
| Don't want a Python env | [audio.cpp](https://github.com/0xShug0/audio.cpp) or [yue2.cpp](https://github.com/engival/yue2.cpp) — C++ runtime + GGUF, no Python required |

> Short on VRAM? Jump to [Quantization & Acceleration](#-quantization--acceleration). Want the prompt recipes? See [Tutorials & Best Practices](#-tutorials--best-practices).

---

## 🏛️ Official Resources

<!-- markdownlint-disable MD034 -->

| Project | Description | Notes |
|---|---|---|
| [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) | Official YuE / YuE2 repo. YuE2 adds symbolic planning (editable ABC scores), zero-shot covers and agentic music editing — quality rivaling Suno v5/v6 | Code Apache-2.0; weights CC BY-NC 4.0 |
| [YuE2 website](https://map-yue2.github.io/) | YuE2 project page with online demo | — |
| [NOIZ online demo](https://yue.noizai.net/) | Try YuE2 free in the browser, no install (recommended in official README) | Online service |
| [Blizaine/Maestro](https://github.com/Blizaine/Maestro) | Local song generation, composition planning and covers, powered by YuE2 (official README) | — |
| [YuE1 demo page](https://map-yue.github.io/) | First-generation YuE demo | — |
| [YuE-v1 branch](https://github.com/multimodal-art-projection/YuE/tree/YuE-v1) | Code, docs and license for the original YuE; YuE1 tools still target this branch | Legacy |
| [arXiv:2609.33757](https://arxiv.org/abs/2609.33757) | **YuE2 technical report**: symbolic planning, zero-shot covers, agentic editing, automatic/expert listening tests and WildSongBench evaluation | 2026.09 |
| [arXiv:2610.05336](https://arxiv.org/abs/2610.05336) | **SheetSage2 paper**: audio-to-lead-sheet transcription (ABC/MIDI), the basis for covers and score editing | 2026.10 |
| [arXiv:2503.08638](https://arxiv.org/abs/2503.08638) | Paper: *YuE: Scaling Open Foundation Models for Long-Form Music Generation* | 2025.03 |
| [m-a-p on Hugging Face](https://huggingface.co/m-a-p) | Official weights and data: YuE2-3B, YuE2-Vae (incl. legacy), SheetSage2, MERT2, WildSongBench, full YuE1 line | — |
| [WildSongBench](https://huggingface.co/datasets/m-a-p/WildSongBench) | Official full-song benchmark: 192 Chinese/English prompts (94 zh / 98 en), evaluation protocol and reproduction scripts | CC BY-NC 4.0 |
| [m-a-p/SheetSage2](https://huggingface.co/m-a-p/SheetSage2) | Official audio-to-score model (MERT2 encoder) producing editable ABC/MIDI; used for covers and score editing | CC BY-NC 4.0 |
| [m-a-p/MERT-v2-FullSong](https://huggingface.co/m-a-p/MERT-v2-FullSong) · [MERT-v2-30s](https://huggingface.co/m-a-p/MERT-v2-30s) | MERT2 music-understanding models (full-song / 30s): SheetSage2 encoder and YuE2 evaluation | CC BY-NC 4.0 |
| [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) | All-in-one checkpoint built with the ComfyUI team (`yue2_3b_bf16.safetensors`, ~7.8 GB) | ComfyUI-specific |
| [Official docs: docs/generation.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/generation.md) | YuE2 generation guide: `SongRequest` / `GenerationConfig` / symbolic score editing / reproducibility | — |
| [Official cover guide: docs/covers.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) | Transcribe a reference recording with SheetSage2 → edit ABC melody → `cot="melody"` to re-sing with new lyrics/style; full commands and examples | — |
| [Official evaluation: docs/benchmarks.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md) | WildSongBench, cover and score-editing evaluation; Suno v5/v6 comparison and reproduction notes | — |
| [Official built-in Skill: yue2-music](https://github.com/multimodal-art-projection/YuE/tree/main/skills/yue2-music) | Agent Skill **v1.2.0 (2026-09-25)**: adds instrumental generation and instrumental covers from ABC/reference audio; includes `run_yue2.py` and the instrumental sub-skill | — |

> **License note**: YuE2 code, Agent Skill and docs are Apache-2.0; model weights are **CC BY-NC 4.0** (free for personal/creator use including monetized outputs; companies need a commercial weight license from the authors).

> **YuE2 architecture at a glance**: a 2.2B AR language model plans the song and semantic tokens (`full`/`melody`/`off` CoT modes) → a 1.5B NAR flow-matching branch generates 64-channel VAE latents → a 48 kHz stereo VAE decodes the output; supports vLLM acceleration, CUDA Graph and weight offload.

## 🖥️ GUIs

> Graphical interfaces — generate songs with one click, low barrier to entry. Entries marked **YuE1** only support the original YuE; YuE2 users should start with the YuE2 apps above.

| Project | Description | Platform | Notes |
|---|---|---|---|
| ⭐ [RevolutionLA/YuE2-Music-Workbench](https://github.com/RevolutionLA/YuE2-Music-Workbench) | Local AI music workstation: YuE2 songwriting + AI covers + RVC voice conversion + LRC synced lyrics + batch queue — 100% offline, ready out of the box | Windows | Featured |
| [timoncool/YuE2-Studio](https://github.com/timoncool/YuE2-Studio) | Local AI song studio (v3.7.0): editable staff score, SheetSage2 covers, instrumental switch, six-stem separation, audio-to-MIDI and built-in LoRA training | Windows/Linux | MIT |
| [scragnog/HOT-Step-CPP](https://github.com/scragnog/HOT-Step-CPP) | C++/GGML desktop music workstation: switch between ACE-Step 1.5, MiniMax-Music3 and YuE2; built-in dataset labelling and native AR/NAR joint LoRA training, no Python | Win/Linux/macOS | MIT |
| [igrbible/Ruach_Studio](https://github.com/igrbible/Ruach_Studio) | Full YuE2 workstation built on yue2.cpp: ABC score editing, two seeds, library/favourites, 200 instrument probes, built-in LoRA training | Windows/NVIDIA | AGPL-3.0 |
| [lvxworld/lux-in-music](https://github.com/lvxworld/lux-in-music) | Local song studio on Apple Silicon via audio.cpp: Vibe style references, stem mixer, section editing | macOS Apple Silicon | MIT |
| [yeufonic/yeufonic](https://github.com/yeufonic/yeufonic) | Web UI + Docker/Windows installer: prompt-to-song and recording covers, ABC editing, stems, LoRA training/import/sharing; runs on ComfyUI + YuE2 nodes | Docker/Win | — |
| [victorcampeanu/OpenSuno-YuE2](https://github.com/victorcampeanu/OpenSuno-YuE2) | Mac/NVIDIA local song studio: Melody/Chords planning, musical sliders (Composition/Weirdness), model arranging, LoRA catalog, re-render from saved tokens | macOS/Win | MIT |
| [deepbeepmeep/YuEGP](https://github.com/deepbeepmeep/YuEGP) | YuEGP (YuE1): optimized for "GPU poor" users, MMGP memory management | Linux/Win | Recommended in YuE-v1 README |
| [joeljuvel/YuE-UI](https://github.com/joeljuvel/YuE-UI) | YuE-UI (YuE1): Gradio UI with batch generation, timeline visualization, incremental continuation and session save/load — runs on 8GB VRAM with quantized models | Cross-platform | Recommended in YuE-v1 README |
| [sgsdxzy/YuE-exllamav2](https://github.com/sgsdxzy/YuE-exllamav2) | ExLlamaV2 accelerated implementation (with GUI) — one of the most efficient YuE1-era inference setups | Linux/Win | Apache-2.0 |
| [alisson-anjos/YuE-exllamav2-UI](https://github.com/alisson-anjos/YuE-exllamav2-UI) | (YuE1) Gradio UI on top of YuE-exllamav2 — 5.45× end-to-end speedup measured on RTX 4090; Docker image available | Linux/Win/Docker | Apache-2.0 |
| [alisson-anjos/YuE-Interface](https://github.com/alisson-anjos/YuE-Interface) | (YuE1) Dockerized Gradio UI — one env var pulls all official/quantized models; deploy locally or on RunPod | Docker/RunPod | — |
| [WrongProtocol/YuE-exllamav2-UI](https://github.com/WrongProtocol/YuE-exllamav2-UI) | The original Gradio UI for YuE-exllamav2 (YuE1; YuE-v1 README) | Linux/Win | — |
| [vrgamegirl19/Yue2_Studio](https://github.com/vrgamegirl19/Yue2_Studio) | YuE2 desktop music studio | Windows | Apache-2.0 |
| [krakenunbound/yue2-studio](https://github.com/krakenunbound/yue2-studio) | Native Windows music studio: local model download, lyrics/cover editing | Windows | — |
| [Ladypoly/YuE2_WebUI](https://github.com/Ladypoly/YuE2_WebUI) | YuE2 WebUI | — | Apache-2.0 |
| [dynamohum/YuE2gen-studio](https://github.com/dynamohum/YuE2gen-studio) | Web UI for cover recording / prompt-based songwriting / editing | — | Apache-2.0 |
| [Mozer/YuE-extend](https://github.com/Mozer/YuE-extend) | YuE1 music continuation (mp3 extend) + GUI, with a Colab version | Cross-platform | Apache-2.0 |
| [CodeCat04/Whiskerwave-Studio](https://github.com/CodeCat04/Whiskerwave-Studio) | Local-first YuE2 generation GUI + Ollama-assisted lyric writing | — | — |
| [DocShotgun/ds-yue-webui](https://github.com/DocShotgun/ds-yue-webui) | YuE2 WebUI: generate / cover / edit | — | — |
| [aidec/YuE-exllamav2-GUI-easy](https://github.com/aidec/YuE-exllamav2-GUI-easy) | (YuE1) Easy-setup GUI for YuE-exllamav2 (Traditional Chinese interface) | Windows | — |
| [LeeAeron/YuE2UI](https://github.com/LeeAeron/YuE2UI) | YuE2 desktop app | — | Apache-2.0 |

## ⚡ Quantization & Acceleration

> Quantized weights and throughput optimizations when VRAM is tight. **YuE2 and YuE1 weights are not compatible**; entries marked YuE1 cannot load YuE2.

| Project | Description | Notes |
|---|---|---|
| [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) | General C++/GGML audio inference engine (3.6k★): YuE2 with ABC planning, AR/NAR LoRA and SheetSage2 transcription; BF16/Q8/Q4 on NVIDIA/AMD/Metal/CPU | Apache-2.0 |
| [NoizAI/YuE2-Turbo](https://github.com/NoizAI/YuE2-Turbo) | YuE2 high-concurrency inference & serving toolkit: same model, same recipe — 1.68× per-song speedup, 3.31× concurrency | Apache-2.0 |
| [audio-cpp/Yue2-3B-GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) | Official audio.cpp YuE2 GGUF: BF16/Q8_0/Q4_0 main model + F32/F16 VAE + sidecars; CLI/WebUI examples included | CC BY-NC 4.0 |
| [Serveurperso/YuE2-GGUF](https://huggingface.co/Serveurperso/YuE2-GGUF) | Pre-quantized GGUF set for yue2.cpp (Q8 3.81 GB + VAE 530 MB, ~5.4 GB total); includes MERT2 / SheetSage2 / realaudio tokenizer | CC BY-NC 4.0 |
| [VincentGOURBIN/yue2-mlx-packs](https://huggingface.co/VincentGOURBIN/yue2-mlx-packs) | Pre-quantized MLX packs for YuE2-3B (int4-mixed-head 2.5 GB / qint8-all-head 3.5 GB / int4-head 4.4 GB), SHA-256 verified on download | CC BY-NC 4.0 |
| [ServeurpersoCom/yue2.cpp](https://github.com/ServeurpersoCom/yue2.cpp) | Portable GGML C++17 implementation + browser UI server: lyrics/style in, 48kHz stereo out; SheetSage2 covers and AR/NAR LoRA | MIT |
| [engival/yue2.cpp](https://github.com/engival/yue2.cpp) | ggml/Vulkan implementation: v0.1.1 ships single-file Windows/Linux binaries; EAGLE-3 speculative decoding, lyrics/ABC file input, mid-song context prompt changes ([demo](https://www.youtube.com/watch?v=gMS2Ko7s97o)) | MIT |
| [WaveCut/YuE2-3B-OrbitQuant-W4A4](https://huggingface.co/WaveCut/YuE2-3B-OrbitQuant-W4A4) | Experimental W4A4 quantization: 3.04 GB (−58% vs BF16), Linux/CUDA, with RTX 4090 speed/VRAM benchmarks | CC BY-NC 4.0 |
| [engival/YuE2-3B-EAGLE3-draft-GGUF](https://huggingface.co/engival/YuE2-3B-EAGLE3-draft-GGUF) | 154 MB EAGLE-3 draft head for speculative decoding in yue2.cpp, accelerating the semantic-token stage | CC BY-NC 4.0 |
| [Alissonerdx exl2 weights](https://huggingface.co/collections/Alissonerdx/yue-models-exllamav2-67a539be76b5225ebda95323) | (YuE1) Full ExLlamaV2 quantization range for YuE-s1-7B (3.0–8.0 bpw) | HF Collection |
| [Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2](https://huggingface.co/Doctor-Shotgun/YuE-s1-7B-anneal-en-cot-exl2) | (YuE1) exl2 quantized weights (Q8/Q6 etc.) | HF |
| [Alissonerdx/YuE-s1-7B-anneal-en-cot-int8](https://huggingface.co/Alissonerdx/YuE-s1-7B-anneal-en-cot-int8) | (YuE1) bitsandbytes INT8 quantized weights | HF |

## 📦 Platform & Local Ports

> Native running and one-click installs on Mac (MLX / Core ML), Windows / Linux and Android, grouped by platform.

| Project | Description | Notes |
|---|---|---|
| [tonywestonuk/YuE-Studio](https://github.com/tonywestonuk/YuE-Studio) | Native Mac app tuned for Apple Silicon (GPU + Neural Engine) | Apache-2.0 |
| [vanch007/mlx-Yue](https://github.com/vanch007/mlx-Yue) | Apple Silicon MLX native port of YuE2-3B (with audio transcription) | Apache-2.0 |
| [ianiv/YuE2](https://github.com/ianiv/YuE2) | YuE2 Studio: local web app on Apple Silicon (MLX) | MIT |
| [VincentGourbin/yue2-mlx-swift](https://github.com/VincentGourbin/yue2-mlx-swift) | Swift/MLX port: lyrics + style → full song | MIT |
| [daig/yue2-mlx](https://github.com/daig/yue2-mlx) | BF16-first MLX/MPS experiments, auto-tracking upstream | Apache-2.0 |
| [arinltte/YuE2Mac](https://github.com/arinltte/YuE2Mac) | Local AI songwriting studio (Mac) | MIT |
| [stavitian/yue2-studio](https://github.com/stavitian/yue2-studio) | macOS app + installer: YuE2-3B generation/cover/transcription (with 24 GB Mac fixes) | — |
| [sdbds/YuE-for-windows](https://github.com/sdbds/YuE-for-windows) | YuE1 native Windows support (Gradio + Docker) | Apache-2.0 |
| [Cognito-Inc-451/Yue2-CUDA-Windows](https://github.com/Cognito-Inc-451/Yue2-CUDA-Windows) | YuE2 CUDA Windows adaptation | — |
| [siliconsense/yue2-studio-pc](https://github.com/siliconsense/yue2-studio-pc) | One-click batch to run YuE2 on NVIDIA GPUs (songs + covers) | — |
| [Rdx-ai-art/yue2-mlx.pinokio](https://github.com/Rdx-ai-art/yue2-mlx.pinokio) | Pinokio one-click installer for YuE2-3B (Mac MLX) | — |
| [deadjoe/yue2_groove](https://github.com/deadjoe/yue2_groove) | Unofficial YuE2 web UI (Apple Silicon first, Linux/CUDA also works), plus a [Pinokio version](https://github.com/deadjoe/yue2-groove-pinokio) | Apache-2.0 |
| [PasiKoodaa/YuE2-Radio](https://github.com/PasiKoodaa/YuE2-Radio) | Local AI radio (continuous YuE2 playback) | MIT |
| [Joker56156/tio-music-studio](https://github.com/Joker56156/tio-music-studio) | Local AI music studio: ACE-Step 1.5 / YuE / DiffRhythm integration | — |
| [JackKnifeAI/killa-yue](https://github.com/JackKnifeAI/killa-yue) | Native Android YuE2 studio (experimental): on-device generation (Snapdragon GPU or CPU), stems, mixer, recording; [APK download](https://github.com/JackKnifeAI/killa-yue/releases) | Apache-2.0 |

## 🧩 ComfyUI Integrations

> ComfyUI natively supports YuE2 (PR #16250, `yue2` branch). Below are community node packs and related workflows; the official [text-to-music workflow template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_yue2_text2music.json) is also available.

| Project | Description | Notes |
|---|---|---|
| ComfyUI native support | Built-in nodes in ComfyUI core (`YuE2GenerateABC` / `YuE2GenerateMusic` etc., in `comfy_extras/nodes_yue2.py`), using the [Comfy-Org/YuE2](https://huggingface.co/Comfy-Org/YuE2) all-in-one checkpoint; CFG control and AMD fixes landed in September 2026 | Official native |
| [smthemex/ComfyUI_YuE](https://github.com/smthemex/ComfyUI_YuE) | Now supports YuE2 and cover mode (loads SheetSage2 + MERT2) while keeping YuE1 Stage A/B and exl2/INT8 quantization | Apache-2.0 |
| [filliptm/ComfyUI-FL-YuE2](https://github.com/filliptm/ComfyUI-FL-YuE2) | YuE2 music generation + editable piano roll | Apache-2.0 |
| [T8mars/Comfyui-YuE2-T8](https://github.com/T8mars/Comfyui-YuE2-T8) | YuE2 ComfyUI node pack | — |
| [ScryptHunter/ComfyUI-YuE2](https://github.com/ScryptHunter/ComfyUI-YuE2) | Compatibility fork with isolated dependencies, adapted for newer ComfyUI and Transformers | Apache-2.0 |
| [pytraveler/YuE2-ComfyUI](https://github.com/pytraveler/YuE2-ComfyUI) | YuE2 nodes with a piano-roll score editor, Edit Track (retake, cut, move or extend parts of a finished song), covers from audio or MIDI, a lyrics writer and LoRA support | Apache-2.0 |
| [KytraScript/ComfyUI-FS_Audio_Suite](https://github.com/KytraScript/ComfyUI-FS_Audio_Suite) | Modular YuE2 audio generation nodes + mastering/denoise workflows (cover generation included) | — |
| [o-l-l-i/ComfyUI-Olm-YuE2](https://github.com/o-l-l-i/ComfyUI-Olm-YuE2) | Style + lyrics → song, optional score view/edit | — |
| [nvmax/ComfyUI-YuE2](https://github.com/nvmax/ComfyUI-YuE2) | YuE2 ComfyUI nodes | Apache-2.0 |
| [piscesbody/ComfyUI-YuE2](https://github.com/piscesbody/ComfyUI-YuE2) | YuE2 ComfyUI nodes (upstream of the ScryptHunter fork) | Apache-2.0 |
| [EmeraldApple-AI/ComfyUI-YuE2](https://github.com/EmeraldApple-AI/ComfyUI-YuE2) | YuE2-3B lyrics-to-song custom node | — |
| [TheLocalLab/ComfyUI-SongScribe](https://github.com/TheLocalLab/ComfyUI-SongScribe) | AI music prompt nodes: 73 style presets + song analysis (supports YuE2) | MIT |
| [UnlimitedEditing/ComfyUI-YuE2Fast](https://github.com/UnlimitedEditing/ComfyUI-YuE2Fast) | Fast nodes running the official YuE2 runtime (CUDA Graph decoding) | — |
| [cicalooo/ComfyUI-YuE2-LongSong](https://github.com/cicalooo/ComfyUI-YuE2-LongSong) | YuE2 long-song generation workflow | MIT |
| [mitnits/yue2-same-music-new-lyrics](https://github.com/mitnits/yue2-same-music-new-lyrics) | Keep the melody, sing new lyrics: Gradio UI + ComfyUI nodes (YuE2 + SheetSage2) | Apache-2.0 |
| [TheAwaken1/ComfyUI-SongLRC](https://github.com/TheAwaken1/ComfyUI-SongLRC) | Write a line-timed `.lrc` next to the generated audio; can use the YuE2 ABC score for timing, works with ComfyUI-FL-YuE2 | MIT |

## 🎚️ Fine-tuning & LoRA

> Both halves of YuE2 (AR planner and NAR acoustic model) can be trained with LoRA. Below: in-ComfyUI trainers, standalone training bases and community adapters. timoncool/YuE2-Studio, Ruach_Studio and yeufonic also include training pages.

| Project | Description | Notes |
|---|---|---|
| [Starnodes2024/ComfyUI-YuE2-Trainer](https://github.com/Starnodes2024/ComfyUI-YuE2-Trainer) | Train a YuE2 style LoRA inside ComfyUI (NAR branch, 24GB VRAM recommended), native ComfyUI format output | — |
| [Starnodes2024/ComfyUI-YuE2-Trainer](https://github.com/Starnodes2024/ComfyUI-YuE2-Trainer) | Train NAR acoustic MODEL LoRAs and AR planner CLIP LoRAs separately inside ComfyUI; loadable by the native YuE2 nodes | Apache-2.0 |
| [Mothersuperior/YuE2-instrumental-cot-full-loras](https://huggingface.co/Mothersuperior/YuE2-instrumental-cot-full-loras) | Instrumental AR LoRA (rank 64, trained on 2.7k instrumental tracks + SheetSage2 ABC); use with `cot="full"` for section-planned instrumentals | CC BY-NC 4.0 |
| [scragnog/YuE2-GGUF](https://huggingface.co/scragnog/YuE2-GGUF) | HOT-Step `int8_convrot` base for joint AR/NAR training (training-only GGUF) with the native C++ trainer | CC BY-NC 4.0 |

## 🎛️ Music Production Toolchain

> Connecting YuE2 to DAWs, score editing, humming input and audio post-production.

| Project | Description | Notes |
|---|---|---|
| [betweentwomidnights/gary4juce](https://github.com/betweentwomidnights/gary4juce) | VST3/AU: brings YuE2 (yuey), MusicGen and 6 more models into your DAW; tempo/key-aware generation, covers/continuation, drag ABC to MIDI, local stem separation | Windows/macOS · AGPL-3.0 |
| [mikkel/yue2-concept-sliders](https://github.com/mikkel/yue2-concept-sliders) | 16 YuE2 music concept sliders, ComfyUI-ready | MIT |
| [nheegen/yue2-session-bridge](https://github.com/nheegen/yue2-session-bridge) | Ableton Max for Live device: Session MIDI harmony → ABC → YuE2 | MIT |
| [Mothersuperior/YuE2-hum-to-song](https://huggingface.co/Mothersuperior/YuE2-hum-to-song) · [HF Space](https://huggingface.co/spaces/Mothersuperior/yue2-hum-to-song) | Hum 10–30 seconds + style/lyrics → a full song that keeps your melody: AR score continuation + NAR prosody adapter, with ComfyUI/script usage | CC BY-NC 4.0 |

## ☁️ Cloud & Serving

| Project | Description | Notes |
|---|---|---|
| [yolanother/runpod-yuegp-serverless](https://github.com/yolanother/runpod-yuegp-serverless) | YuEGP worker on RunPod Serverless | — |
| [lee101/yue-cog](https://github.com/lee101/yue-cog) | Cog packaging for YuE2 + RunPod serverless adapter | — |
| [sruckh/Yue2-runpod](https://github.com/sruckh/Yue2-runpod) | YuE2 RunPod Serverless worker (style + lyrics → full song) | — |
| [Sparaa/yue2-sidecar](https://github.com/Sparaa/yue2-sidecar) | FastAPI task API (built on yue2-infer, ABC covers and long songs) | Apache-2.0 |
| [arthurfarache/muvflow-yue](https://github.com/arthurfarache/muvflow-yue) | YuE music generation API (SaladCloud) | — |
| [giapnguyen74/yue2-server](https://github.com/giapnguyen74/yue2-server) | YuE2 model server | — |
| [John-yg-Yim/LastAlbum-music-api](https://github.com/John-yg-Yim/LastAlbum-music-api) | FastAPI song generation service based on YuE (LastAlbum backend) | — |
| [usamireko/YuE-exllamav2-Colab](https://github.com/usamireko/YuE-exllamav2-Colab) | One-click YuE-exllamav2 on Google Colab | Apache-2.0 |

## 📚 Tutorials & Best Practices

- **Official prompt engineering guide**: [how to write genre.txt / lyrics.txt](https://github.com/multimodal-art-projection/YuE#prompt-engineering) — song section tags (`[Verse]`/`[Chorus]`), style tag ordering, etc.
- **Official sample workflow videos**: Fahd's [YuE quick-start video](https://github.com/multimodal-art-projection/YuE#quick-start).
- **YuE2 prompt structure**: put genre/instruments/vocals/language/tempo in `style`, tagged lyrics in `lyrics`; see [examples/song.json](https://github.com/multimodal-art-projection/YuE/blob/main/examples/song.json).
- **ICL cover best practices** (excerpt from the official README):
  1. Dual-track ICL (vocal + accompaniment) gives the best musicality and prompt adherence;
  2. A chorus excerpt works better as reference audio;
  3. About 30 seconds of reference audio is ideal;
  4. Separate stems with [python-audio-separator](https://github.com/nomadkaraoke/python-audio-separator) or UVR;
  5. Providing reference audio reduces diversity — pure CoT mode yields more varied output.
- **Official cover workflow**: [docs/covers.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/covers.md) — transcribe a reference recording with SheetSage2 → edit the ABC melody → `cot="melody"` → new lyrics/style; start with `examples/melody.abc`.
- **Official evaluation and reproduction**: [docs/benchmarks.md](https://github.com/multimodal-art-projection/YuE/blob/main/docs/benchmarks.md) + [WildSongBench](https://huggingface.co/datasets/m-a-p/WildSongBench) — 192 Chinese/English prompts, Suno v5/v6 comparison and standard YuE2 reproduction steps.
- **Windows local deployment (Bilibili + written guide)**: [eogee video](https://www.bilibili.com/video/BV1esaw62EJx) / [article](https://eogee.com/article/148) — runs YuE2 on Windows with the ComfyUI portable package, including ABC score editing and melody reuse.
- **Local deployment and score white-box walkthrough**: [Algieba's blog](https://blog.algieba12.cn/yue2-local-deployment-and-practice/) — uv + ModelScope acceleration in China, SheetSage2 covers, and a layer-by-layer look at generated artifacts.
- **HyperAI cloud notebook**: [YuE2-3B tutorial](https://next.hyper.ai/cn/notebooks/yue2-3b-frontier-open-music-generation) — Gradio Create/Cover tabs; useful without a local GPU.
- **ComfyUI Wiki: YuE2-3B intro and native support**: [comfyui-wiki.com/en/news/2026-09-11-yue2-3b](https://comfyui-wiki.com/en/news/2026-09-11-yue2-3b) — includes ComfyUI dependency conflict notes (PyTorch/Transformers version pins).
- **DeepWiki: YuE code walkthrough**: [deepwiki.com/multimodal-art-projection/YuE](https://deepwiki.com/multimodal-art-projection/YuE) — visualized docs for `YuE2Pipeline` architecture, AR/NAR/VAE modules and backend acceleration.
- **VRAM cheat sheet (YuE2)**: 24GB+ → official BF16; 12–16GB → Q8 GGUF / FP8; 8GB → Q4/Q8 GGUF (audio.cpp / yue2.cpp, community reports 8–9GB); Mac → MLX / audio.cpp Metal. YuE1's YuEGP / YuE-UI cannot load YuE2.

## 🔗 Related Projects

| Project | Description |
|---|---|
| [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) | Another open-source music generation foundation model (13.8k★), often compared/combined with YuE2; remiqora and HOT-Step integrate both in one UI |
| [inikolax/remiqora](https://github.com/inikolax/remiqora) | Local studio unifying ACE-Step 1.5 and YuE2-3B (v0.4.1): YuE2 runs on audio.cpp's native server, with Demucs stems, a multitrack editor and a LoRA training UI |

## 👥 Community

- [GitHub Issues / Discussions](https://github.com/multimodal-art-projection/YuE/issues) — official issues and roadmap; recent PRs focus on the vLLM V2 sampler, Intel XPU and MPS/Windows CUDA fixes, while feature requests cluster around multi-vocalist generation, time signatures and per-section vocal control.
- [Official Discord](https://discord.gg/ssAyWMnMzu) — YuE2 community discussion and sharing.
- [Hugging Face m-a-p org](https://huggingface.co/m-a-p) — weights, datasets and model cards.
- [map-yue2.github.io](https://map-yue2.github.io/) — online listening demo.
- **Milestone (2026-09)**: YuE2 reached GitHub Trending #1 and Hugging Face Text-to-Audio Trending #1 (official README badges).

## 🤝 Contributing

PRs welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria, formatting rules and submission steps. Both English and Chinese submissions are accepted; English is preferred here.

## ⚖️ License

This list is released under [CC0 1.0](LICENSE). Listed projects retain their own licenses — check each project's page before use.

---

<div align="center">

**[⬆ Back to top](#-awesome-yue)**

Made with ❤️ by the YuE community · Inspired by [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) & [sindresorhus/awesome](https://github.com/sindresorhus/awesome)

</div>
