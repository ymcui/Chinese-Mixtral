[**🇨🇳中文**](./README.md) | [**🌐English**](./README_EN.md) | [**📖文档/Docs**](https://github.com/ymcui/Chinese-Mixtral/wiki) | [**❓提问/Issues**](https://github.com/ymcui/Chinese-Mixtral/issues) | [**💬讨论/Discussions**](https://github.com/ymcui/Chinese-Mixtral/discussions) | [**⚔️竞技场/Arena**](http://llm-arena.ymcui.com/)

<p align="center">
    <br>
    <img src="./pics/banner.png" width="800"/>
    <br>
</p>
<p align="center">
    <img alt="GitHub" src="https://img.shields.io/github/license/ymcui/Chinese-Mixtral.svg?color=blue&style=flat-square">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ymcui/Chinese-Mixtral">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/ymcui/Chinese-Mixtral">
    <a href="https://app.codacy.com/gh/ymcui/Chinese-Mixtral/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/142d688425494644b5b156068f55370d"/></a>
</p>

本项目基于Mistral.ai发布的[Mixtral模型](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)进行开发，该模型使用了稀疏混合专家模型（Sparse MoE）架构。本项目利用大规模中文无标注数据进行了中文增量训练，得到了**中文Mixtral**基础模型，并且进一步通过指令精调，得到了**中文Mixtral-Instruct**指令模型。该模型原生支持**32K上下文（实测支持64K+）**，能够有效地处理长文本，同时在数学推理、代码生成等方面获得了显著性能提升。使用llama.cpp进行量化推理时，最低只需16G内存（或显存）。

#### 本项目主要内容

- 🚀 开源中文Mixtral基础模型，该模型在[Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)的基础上进行了中文增量训练
- 🚀 开源中文Mixtral-Instruct指令模型，该模型在中文Mixtral的基础上进一步进行了指令精调
- 🚀 开源了预训练脚本、指令精调脚本，用户可根据需要进一步训练或微调模型
- 🚀 提供了利用个人电脑CPU/GPU快速在本地进行大模型量化和部署的教程
- 🚀 支持[🤗transformers](https://github.com/huggingface/transformers), [llama.cpp](https://github.com/ggerganov/llama.cpp), [text-generation-webui](https://github.com/oobabooga/text-generation-webui), [LangChain](https://github.com/hwchase17/langchain), [privateGPT](https://github.com/imartinez/privateGPT), [vLLM](https://github.com/vllm-project/vllm)等Mixtral生态

----

[中文LLaMA-2&Alpaca-2大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2) | [中文LLaMA&Alpaca大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | [多模态中文LLaMA&Alpaca大模型](https://github.com/airaria/Visual-Chinese-LLaMA-Alpaca) | [多模态VLE](https://github.com/iflytek/VLE) | [中文MiniRBT](https://github.com/iflytek/MiniRBT) | [中文LERT](https://github.com/ymcui/LERT) | [中英文PERT](https://github.com/ymcui/PERT) | [中文MacBERT](https://github.com/ymcui/MacBERT) | [中文ELECTRA](https://github.com/ymcui/Chinese-ELECTRA) | [中文XLNet](https://github.com/ymcui/Chinese-XLNet) | [中文BERT](https://github.com/ymcui/Chinese-BERT-wwm) | [知识蒸馏工具TextBrewer](https://github.com/airaria/TextBrewer) | [模型裁剪工具TextPruner](https://github.com/airaria/TextPruner) | [蒸馏裁剪一体化GRAIN](https://github.com/airaria/GRAIN)


## 新闻

**[2024/??/??] 🚀 正式发布Chinese-Mixtral（基座模型），Chinese-Mixtral-Instruct（指令/chat模型）。详情查看：[📚v1.0版本发布日志](https://github.com/ymcui/Chinese-Mixtral/releases/tag/v1.0)**


## 内容导引
| 章节                                  | 描述                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| [💁🏻‍♂️模型简介](#模型简介) | 简要介绍本项目相关模型的技术特点 |
| [⏬模型下载](#模型下载)        | 中文Mixtral大模型下载地址    |
| [💻推理与部署](#推理与部署) | 介绍了如何对模型进行量化并使用个人电脑部署并体验大模型 |
| [💯模型效果](#模型效果) | 介绍了模型在部分任务上的效果    |
| [📝训练与精调](#训练与精调) | 介绍了如何训练和精调中文Mixtral大模型 |
| [❓常见问题](#常见问题) | 一些常见问题的回复 |


## 模型简介

本项目开源了基于[Mixtral模型](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)开发的中文Mixtral、中文Mixtral-Instruct模型，其主要特点如下：

#### 📖 稀疏混合专家模型

Mixtral是一个稀疏混合专家模型。该模型与以往的LLaMA等主流大模型结构具有显著差异，主要体现在以下几点：

- 每个FFN层包含8个不同的"专家"（全连接层），根据门控值选取最优的2个进行激活
- 输入序列中的每个token都会独立地选取专家，而不是整个序列对应一组专家
- 实际参数量约为46.7B，在推理时激活的参数量约为13B

#### 🚄 原生支持32K上下文

与[Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)以及[Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)项目不同，Mixtral模型原生支持32K上下文（实测支持64K+）。用户可使用单一模型来解决不同长度的各类任务。

## 模型下载

### 模型选择指引

以下是本项目的模型对比以及建议使用场景。**如需聊天交互，请选择Instruct版。**

| 对比项                | 中文Mixtral                                     | 中文Mixtral-Instruct                                  |
| :-------------------- | :----------------------------------------------------: | :----------------------------------------------------------: |
| 模型类型 | **基座模型** | **指令/Chat模型（类ChatGPT）** |
| 模型大小 | 8x7B（实际激活约13B） | 8x7B（实际激活约13B） |
| 专家数量 | 8个（实际激活2个） | 8个（实际激活2个） |
| 训练类型     | Causal-LM (CLM)           | 指令精调                                                     |
| 训练方式 | QLoRA + 全量emb/lm-head | QLoRA + 全量emb/lm-head |
| 基于什么模型训练 | 原版Mixtral-8x7B-v0.1 | 中文Mixtral |
| 训练语料 | 无标注通用语料 | 有标注指令数据 |
| 词表大小 | 原版词表，32000 | 原版词表，32000 |
| 支持上下文长度 | 32K（实测支持64K+） | 32K（实测支持64K+） |
| 输入模板              | 不需要                                                 | 需要套用Mixtral-Instruct模板 |
| 适用场景            | 文本续写：给定上文，让模型生成下文            | 指令理解：问答、写作、聊天、交互等 |
| 不适用场景          | 指令理解 、多轮聊天等                                  |  文本无限制自由生成                                                       |


### 下载地址

以下提供了3种不同类型的模型：

- **完整版模型**：直接下载即可使用，无需其他合并步骤，推荐网络带宽充足的用户；
- **LoRA版模型**：无法单独使用，必须与原版[Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)合并才能转为完整版模型，推荐网络带宽不足且手头有原版Mixtral的用户。合并方法请参阅：【LINK-TBA】
- **GGUF版模型**：兼容[llama.cpp](https://github.com/ggerganov/llama.cpp)等工具的GGUF量化版模型，推荐只需要做推理部署的用户下载。

| 模型名称                  |   类型   |                    完整版（94 GB）                    |                    LoRA版（2.4 GB）                    |                    GGUF版                    |
| :------------------------ | :------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| Chinese-Mixtral | 基座模型 | [[Baidu]](https://pan.baidu.com/s/1nwJ8JkMTUrCkDEccg7C9Pw?pwd=33kb) [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral) | [[Baidu]](https://pan.baidu.com/s/1XRw2-rumi-Pg0CrXqEh8ug?pwd=8gjk) [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-lora) | [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-gguf) |
| Chinese-Mixtral-Instruct | 指令模型 | [Baidu] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct) | [Baidu] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct-lora) | [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct-gguf) |

> [!NOTE]
> 若无法访问HF，可考虑一些镜像站点（如hf-mirror.com），具体方法请自行查找解决。

## 推理与部署

本项目中的相关模型主要支持以下量化、推理和部署方式，具体内容请参考对应教程。

| 工具   | 特点     | CPU  | GPU  | 量化 | GUI  | API  | vLLM |                      教程                             |
| :----------------------------------------------------------- | ---------------------------- | :--: | :--: | :--: | :--: | :--: | :--: |:--: |
| [llama.cpp](https://github.com/ggerganov/llama.cpp)      | 丰富的量化选项和高效本地推理 |  ✅   |  ✅   |  ✅   |  ❌   |  ✅   |  ❌   | [link] |
| [🤗Transformers](https://github.com/huggingface/transformers) | 原生transformers推理接口     |  ✅   |  ✅   |  ✅   |  ✅   |  ❌   |  ✅  | [link] |
| [仿OpenAI API调用](https://platform.openai.com/docs/api-reference) | 仿OpenAI API接口的服务器Demo |  ✅   |  ✅   |  ✅   |  ❌   |  ✅   |  ✅  | [link] |
| [text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 前端Web UI界面的部署方式 |  ✅   |  ✅   |  ✅   |  ✅   |  ✅  | ❌  | [link] |
| [LangChain](https://github.com/hwchase17/langchain) | 适合二次开发的大模型应用开源框架 |  ✅  |  ✅   |  ✅   |  ❌   |  ❌   | ❌  | [link] |
| [privateGPT](https://github.com/imartinez/privateGPT) | 多文档本地问答框架 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | [link] |


## 模型效果

为了评测相关模型的效果，本项目分别进行了生成效果评测和客观效果评测（NLU类），从不同角度对大模型进行评估。需要注意的是，综合评估大模型能力仍然是亟待解决的重要课题，单个数据集的结果并不能综合评估模型性能。推荐用户在自己关注的任务上进行测试，选择适配相关任务的模型。

### 生成效果评测

为了更加直观地了解模型的生成效果，本项目仿照[Fastchat Chatbot Arena](https://chat.lmsys.org/?arena)推出了模型在线对战平台，可浏览和评测模型回复质量。对战平台提供了胜率、Elo评分等评测指标，并且可以查看两两模型的对战胜率等结果。

**⚔️ 模型竞技场：[http://llm-arena.ymcui.com](http://llm-arena.ymcui.com/)**

| 系统                         | 对战胜率（无平局） ↓ | Elo评分 |
| ---------------------------- | :------------------: | :-----: |
| **Chinese-Mixtral-Instruct** |                      |         |
| Chinese-Alpaca-2-7B-RLHF     |                      |         |
| Chinese-Alpaca-2-7B-64K      |                      |         |
| Chinese-Alpaca-2-13B-16K     |                      |         |
| Chinese-Alpaca-2-7B-16K      |                      |         |
| Chinese-Alpaca-2-13B         |                      |         |
| Chinese-Alpaca-2-7B          |                      |         |


> [!NOTE]
> 以上结果截至2023年9月1日。最新结果请进入[**⚔️竞技场**](http://llm-arena.ymcui.com/)进行查看。

### 客观效果评测

#### C-Eval

[C-Eval](https://cevalbenchmark.com)是一个全面的中文基础模型评估套件，其中验证集和测试集分别包含1.3K和12.3K个选择题，涵盖52个学科。实验结果以“zero-shot / 5-shot”进行呈现。C-Eval推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/ceval_zh)

| Models             | 类型 | Valid (0-shot) | Valid (5-shot) | Test (0-shot) | Test (5-shot) |
| ------------------------ | :------------: | :------------: | :-----------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct | 指令 |                |                |               |               |
| Chinese-Mixtral          | 基座 |                |                |               |               |
| [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) | 基座 | | | | |
| Chinese-Alpaca-2-13B | 指令 | 44.3 | 45.9 | 42.6 | 44.0 |
| Chinese-LLaMA-2-13B | 基座 | 40.6 | 42.7 | 38.0 | 41.6 |


#### CMMLU

[CMMLU](https://github.com/haonan-li/CMMLU)是另一个综合性中文评测数据集，专门用于评估语言模型在中文语境下的知识和推理能力，涵盖了从基础学科到高级专业水平的67个主题，共计11.5K个选择题。CMMLU推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/cmmlu_zh)

| Models             | 类型 | Test (0-shot) | Test (5-shot) |
| ------------------------ | :------------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct | 指令 |               |               |
| Chinese-Mixtral          | 基座 |               |               |
| [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) | 基座 | | |
| Chinese-Alpaca-2-13B | 指令 |     43.2      |     45.5      |
| Chinese-LLaMA-2-13B | 基座 |     38.9      |     42.5      |

#### MMLU

[MMLU](https://github.com/hendrycks/test)是一个用于评测自然语言理解能力的英文评测数据集，是当今用于评测大模型能力的主要数据集之一，其中验证集和测试集分别包含1.5K和14.1K个选择题，涵盖57个学科。MMLU推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/mmlu_zh)

| Models             | 类型 | Valid (0-shot) | Valid (5-shot) | Test (0-shot) | Test (5-shot) |
| ------------------------ | :------------: | :------------: | :-----------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct | 指令 |                |                |               |               |
| Chinese-Mixtral          | 基座 |                |                |               |               |
| [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) | 基座 | | | | |
| Chinese-Alpaca-2-13B | 指令 |                |                |               |               |
| Chinese-LLaMA-2-13B | 基座 |                |                |               |               |

### 长上下文版模型评测

[LongBench](https://github.com/THUDM/LongBench)是一个大模型长文本理解能力的评测基准，由6大类、20个不同的任务组成，多数任务的平均长度在5K-15K之间，共包含约4.75K条测试数据。以下是本项目长上下文版模型在该中文任务（含代码任务）上的评测效果。LongBench推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/longbench_zh)

| Models                   | 单文档QA | 多文档QA | 摘要 | FS学习 | 代码补全 | 合成任务 | 平均 |
| ------------------------ | :------: | :------: | :--: | :----: | :------: | :------: | :--: |
| Chinese-Mixtral-Instruct |          |          |      |        |          |          |      |
| Chinese-Mixtral          |          |          |      |        |          |          |      |
| Chinese-Alpaca-2-13B-16K |   47.9   |   26.7   | 13.0 |  22.3  |   46.6   |   21.5   | 29.7 |
| Chinese-LLaMA-2-13B-16K  |   36.7   |   17.7   | 3.1  |  29.8  |   13.8   |   3.0    | 17.3 |
| Chinese-Alpaca-2-7B-64K  |   44.7   |   28.1   | 14.4 |  39.0  |   44.6   |   5.0    | 29.3 |
| Chinese-LLaMA-2-7B-64K   |   27.2   |   16.4   | 6.5  |  33.0  |   7.8    |   5.0    | 16.0 |

### 量化效果评测

在llama.cpp下，测试了Chinese-Mixtral量化版模型的性能，如下表所示。

|              |  F16 |   Q8_0 |   Q6_K |   Q5_K |   Q5_0 |   Q4_K |   Q4_0 |   Q3_K |   Q2_K | IQ2_XS | IQ2_XXS |
| ------------ | ---: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | -----: | ------: |
| Size (GB)    | 87.0 |   46.2 |   35.7 |   30.0 |   30.0 |   24.6 |   24.6 |   19.0 |   16.1 |   12.7 |    11.4 |
| BPW          | 16.0 |   8.50 |   6.57 |   5.69 |   5.52 |   4.87 |   4.53 |   3.86 |   2.96 |   2.34 |    2.10 |
| PPL          |    - | 4.4076 | 4.4092 | 4.4192 | 4.4224 | 4.4488 | 4.4917 | 4.5545 | 5.1846 | 6.9784 |  8.5981 |
| M3 Max Speed |    - |      - |   36.0 |   36.9 |   35.7 |   31.2 |   27.8 |   37.6 |   29.1 |      - |       - |
| A100 Speed   |    - |      - |   29.9 |   22.6 |   20.5 |   21.7 |   17.1 |   21.7 |   20.3 |   23.7 |    22.5 |

> [!NOTE]
>
> - 模型大小：单位GB
> - BPW（Bits-Per-Weight）：单位参数比特，例如Q6_K实际平均精度为6.57
> - PPL（困惑度）：以4K上下文测量，数值越低越好
> - 生成速度：提供了Apple M3 Max（Metal）以及NVIDIA A100（40G）的生成速度（单位ms/token），数值越低越好

以Chinese-Mixtral-Q4_0为例，下图展示了不同上下文长度下的PPL变化趋势。**实测Mixtral模型支持的上下文长度已超过标称的32K，在64K+上下文下仍然具有较好的表现。**
<p align="center">
    <br>
    <img src="./pics/chinese-mixtral-ppl.png" width="800"/>
    <br>
</p>

## 训练与精调

### 预训练

- 在原版Mixtral的基础上，利用大规模无标注数据进行增量训练，得到Chinese-Mixtral基座模型
- 训练数据采用了一期项目中Plus版本模型一致的数据，其总量约120G纯文本文件
- 训练代码及使用教程：[📖预训练脚本Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/pt_scripts_zh)

### 指令精调

- 在Chinese-Mixtral的基础上，利用有标注指令数据进行进一步精调，得到Chinese-Mixtral-Instruct指令模型
- 训练数据采用了[Chinese-LLaMA-Alpaca-2](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)项目中使用的指令数据，其总量约500万条指令数据
- 训练代码及使用教程：[📖指令精调脚本Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/sft_scripts_zh)

[指令模板](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1#instruction-format)：

```
<s> [INST] Instruction [/INST] Model answer</s> [INST] Follow-up instruction [/INST]
```
注意：`<s>`和`</s>`是表示序列开始和结束的特殊token，而`[INST]`和`[/INST]`则是普通字符串。

## 常见问题

请在提Issue前务必先查看FAQ中是否已存在解决方案。具体问题和解答请参考本项目 [📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/faq_zh)

```
TBA
```


## 引用

TBA


## 免责声明

本项目基于由Mistral.ai发布的Mixtral模型进行开发，使用过程中请严格遵守Mixtral的开源许可协议。如果涉及使用第三方代码，请务必遵从相关的开源许可协议。模型生成的内容可能会因为计算方法、随机因素以及量化精度损失等影响其准确性，因此，本项目不对模型输出的准确性提供任何保证，也不会对任何因使用相关资源和输出结果产生的损失承担责任。如果将本项目的相关模型用于商业用途，开发者应遵守当地的法律法规，确保模型输出内容的合规性，本项目不对任何由此衍生的产品或服务承担责任。


## 问题反馈
如有疑问，请在GitHub Issue中提交。礼貌地提出问题，构建和谐的讨论社区。

- 在提交问题之前，请先查看FAQ能否解决问题，同时建议查阅以往的issue是否能解决你的问题。
- 提交问题请使用本项目设置的Issue模板，以帮助快速定位具体问题。
- 重复以及与本项目无关的issue会被[stable-bot](https://github.com/marketplace/stale)处理，敬请谅解。
