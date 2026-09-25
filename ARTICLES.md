# 推广素材 · 成稿文章

> 这里存放可以直接复制发布的成稿。原则：**文章本身要有独立价值**，清单链接只在文末出现一次——读者是为内容来的，不是为链接来的。
> 配图统一用 [`assets/social-preview.png`](assets/social-preview.png)。

---

## 文章一：本地跑 YuE2 全方案横评：8GB / 16GB / 24GB 显存到底该怎么选

**适用**：知乎、B站专栏、公众号、V2EX、即刻
**状态**：成稿，可直接发布（发布前建议替换文中的实测数据为你自己的）

---

YuE2 发布之后，GitHub 上冒出了一大堆相关工具：GUI、量化版、ComfyUI 节点、Mac 移植、云端模板……多到让人挑花眼。更麻烦的是，很多教程上来就让你装环境，装完才发现显存不够。

这篇文章换个思路：**先按你的硬件分档，再给对应方案**。看完你应该能在 3 分钟内确定自己该装哪个。

### 一、门槛到底在哪

先说清楚 YuE2 是什么结构：

> 2.2B 的自回归语言模型负责"规划"这首歌（写乐谱、生成语义 token）→ 1.5B 的 flow-matching 分支生成声学 latent → 48kHz 立体声 VAE 解码出音频。

官方给的推荐配置是 **Linux + Python 3.12 + 支持 BF16 的 N 卡 + 24GB 显存**。

所以真正的门槛只有一个：**显存**。24GB 能跑原版，往下就得靠量化或显存管理。搞清楚这一点，选型就简单了。

### 二、24GB 及以上：官方原味

不折腾的话，这就是最优解。

```bash
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv && source .venv/bin/activate
python -m pip install .
python examples/generate.py --output outputs/first-song
```

官方支持 vLLM 加速、CUDA Graph 和权重 offload，质量也最好。

值得一提的还有官方自带的 **Agent Skill**（`yue2-music`）：你可以用自然语言跟它聊"把副歌的萨克斯换成钢琴"，它去改 ABC 乐谱再重新渲染。这个思路比反复抽卡靠谱得多。

想要可视化工作流，用 **ComfyUI 原生节点**（配 `Comfy-Org/YuE2` 一体化 checkpoint，约 7.8GB）。

### 三、16GB：走量化

显存差一档，量化是性价比最高的方案：

- **exl2**（ExLlamaV2）：档位最全，3.0–8.0 bpw 可选，按显存挑
- **INT8**（bitsandbytes）：简单直接

社区实测在 RTX 4090 上，exl2 方案端到端能到 **5.45× 提速**——量化不只是"能跑"，往往还更快。代价是音质有轻微损失，但这个档位下你没有别的选择。

### 四、8GB：显存管理 + 量化双管齐下

8GB 就别想 BF16 了，得靠工具把显存压榨到极致：

- **YuEGP**：为"显卡穷人"设计，用 MMGP 做显存管理，**官方 README 亲自推荐**
- **YuE-UI**：Gradio 界面，8GB 可跑，还带批量生成、时间线可视化、增量续写、会话保存

这一档的目标不是"质量最好"，而是"确实能跑出歌来"。能跑通，再谈优化。

### 五、Mac 用户：MLX 生态已经很成熟了

Apple Silicon 用户不用羡慕 N 卡：

- **mlx-Yue**：YuE2-3B 的 MLX 原生移植
- **YuE-Studio**：原生 Mac App，针对 GPU + 神经引擎调优
- **Pinokio 一键安装包**：不想折腾命令行就用这个

注意 MLX 方案迭代很快，跟着上游走就行。另外 24GB 内存的 Mac 有已知问题，有人专门做了修复分支。

### 六、Windows：开箱即用方案

Windows 用户以前最难受，现在有几个真正省事的：

- **YuE2-Music-Workbench**：100% 离线开箱即用，写歌 + AI 翻唱 + RVC 换声 + LRC 滚动歌词 + 批量队列，一套齐活
- **一键批处理脚本**：不想配环境就跑个 bat

### 七、完全不想装 Python？

有 **yue2.cpp**：GGML/Vulkan 实现，一个 C++ 可执行文件，不需要 Python 环境。文本 + 歌词进，48kHz 立体声出。适合想塞进别的应用里的场景。

### 八、想接进自己的工作流

这才是 YuE2 比在线工具强的地方：

- **ComfyUI**：原生节点 + 15 个社区节点包，可以做可编辑钢琴卷帘、训练自己的风格 LoRA、长歌曲生成、母带降噪
- **Ableton**：有 Max for Live 设备，把 Session 里的 MIDI 和声转成 ABC 再喂给 YuE2
- **概念滑杆**：16 个音乐概念滑杆，直接调"明亮度""鼓点密度"这类抽象属性

### 九、只想调 API

- **RunPod Serverless**：三个现成 worker，按次付费
- **Cog**：打包成标准镜像
- **yue2-sidecar**：FastAPI 任务接口，支持 ABC 翻唱和长歌

### 十、给新人的上手路线

1. **先别装任何东西**——去 NOIZ 在线 Demo 听一下效果，确认这东西是你要的
2. 确定本地跑 → 按上面显存分档选方案
3. 先原样跑通官方的 `examples/song.json`，再动提示词
4. 提示词结构：`style` 写流派/乐器/人声/语言/速度，`lyrics` 写带 `[Verse]` `[Chorus]` 标签的歌词
5. 做翻唱时：**双轨 ICL**（人声轨 + 伴奏轨）效果最好，参考音频用副歌片段、30 秒左右；用 `python-audio-separator` 或 UVR 分轨

### 几个容易踩的坑

- **ComfyUI 依赖冲突**：PyTorch / Transformers 版本要 pin，comfyui-wiki 那篇教程里有具体版本
- **提供参考音频会降低多样性**：想要更多变的结果就用纯 CoT 模式，别给参考
- **量化不是无损**：exl2 档位越低音质损失越大，8GB 档位要有心理预期

---

**本文只覆盖了主要方案，完整清单（70+ 项目，含 ComfyUI 节点、DAW 桥接、云部署模板、LoRA 训练器等）在这里持续更新：**

**https://github.com/RevolutionLA/awesome-YuE**

---

## 待写选题

按优先级排列，素材都在清单里，随时可以开工：

1. **《不想付 Suno 订阅费？开源替代 YuE2 的完整本地部署指南》** — 直击最精准人群与搜索词
2. **《Mac 上跑 YuE2：MLX 移植现状》** — 受众窄但极精准，中文资料几乎空白
3. **《把 YuE2 接进 ComfyUI：从原生节点到 LoRA 训练》** — ComfyUI 社区体量大、转发意愿高
4. **《我用 YuE2 做了一首歌：从提示词到分轨母带的完整过程》** — 过程记录型，可读性强
