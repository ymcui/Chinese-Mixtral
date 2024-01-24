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


本项目基于Meta发布的可商用大模型[Llama-2](https://github.com/facebookresearch/llama)开发，是[中文LLaMA&Alpaca大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca)的第二期项目，开源了**中文LLaMA-2基座模型和Alpaca-2指令精调大模型**。这些模型**在原版Llama-2的基础上扩充并优化了中文词表**，使用了大规模中文数据进行增量预训练，进一步提升了中文基础语义和指令理解能力，相比一代相关模型获得了显著性能提升。相关模型**支持FlashAttention-2训练**。标准版模型支持4K上下文长度，**长上下文版模型支持16K、64k上下文长度**。**RLHF系列模型**为标准版模型基础上进行人类偏好对齐精调，相比标准版模型在**正确价值观体现**方面获得了显著性能提升。

#### 本项目主要内容

- 🚀 针对Llama-2模型扩充了**新版中文词表**，开源了中文LLaMA-2和Alpaca-2大模型
- 🚀 开源了预训练脚本、指令精调脚本，用户可根据需要进一步训练模型
- 🚀 使用个人电脑的CPU/GPU快速在本地进行大模型量化和部署体验
- 🚀 支持[🤗transformers](https://github.com/huggingface/transformers), [llama.cpp](https://github.com/ggerganov/llama.cpp), [text-generation-webui](https://github.com/oobabooga/text-generation-webui), [LangChain](https://github.com/hwchase17/langchain), [privateGPT](https://github.com/imartinez/privateGPT), [vLLM](https://github.com/vllm-project/vllm)等Mixtral生态

![](./pics/screencast.gif)

----

[中文LLaMA-2&Alpaca-2大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2) | [中文LLaMA&Alpaca大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | [多模态中文LLaMA&Alpaca大模型](https://github.com/airaria/Visual-Chinese-LLaMA-Alpaca) | [多模态VLE](https://github.com/iflytek/VLE) | [中文MiniRBT](https://github.com/iflytek/MiniRBT) | [中文LERT](https://github.com/ymcui/LERT) | [中英文PERT](https://github.com/ymcui/PERT) | [中文MacBERT](https://github.com/ymcui/MacBERT) | [中文ELECTRA](https://github.com/ymcui/Chinese-ELECTRA) | [中文XLNet](https://github.com/ymcui/Chinese-XLNet) | [中文BERT](https://github.com/ymcui/Chinese-BERT-wwm) | [知识蒸馏工具TextBrewer](https://github.com/airaria/TextBrewer) | [模型裁剪工具TextPruner](https://github.com/airaria/TextPruner) | [蒸馏裁剪一体化GRAIN](https://github.com/airaria/GRAIN)


## 新闻

[2023/07/19] 🚀启动[中文LLaMA-2、Alpaca-2开源大模型项目](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)


## 内容导引
| 章节                                  | 描述                                                         |
| ------------------------------------- | ------------------------------------------------------------ |
| [💁🏻‍♂️模型简介](#模型简介) | 简要介绍本项目相关模型的技术特点 |
| [⏬模型下载](#模型下载)        | 中文Mixtral大模型下载地址    |
| [💻推理与部署](#推理与部署) | 介绍了如何对模型进行量化并使用个人电脑部署并体验大模型 |
| [💯系统效果](#系统效果) | 介绍了模型在部分任务上的效果    |
| [📝训练与精调](#训练与精调) | 介绍了如何训练和精调中文Mixtral大模型 |
| [❓常见问题](#常见问题) | 一些常见问题的回复 |


## 模型简介

本项目推出了基于Llama-2的中文LLaMA-2以及Alpaca-2系列模型，相比[一期项目](https://github.com/ymcui/Chinese-LLaMA-Alpaca)其主要特点如下：

#### 📖 经过优化的中文词表

- 在[一期项目](https://github.com/ymcui/Chinese-LLaMA-Alpaca)中，我们针对一代LLaMA模型的32K词表扩展了中文字词（LLaMA：49953，Alpaca：49954）
- 在本项目中，我们**重新设计了新词表**（大小：55296），进一步提升了中文字词的覆盖程度，同时统一了LLaMA/Alpaca的词表，避免了因混用词表带来的问题，以期进一步提升模型对中文文本的编解码效率

#### ⚡ 基于FlashAttention-2的高效注意力

- [FlashAttention-2](https://github.com/Dao-AILab/flash-attention)是高效注意力机制的一种实现，相比其一代技术具有**更快的速度和更优化的显存占用**
- 当上下文长度更长时，为了避免显存爆炸式的增长，使用此类高效注意力技术尤为重要
- 本项目的所有模型均使用了FlashAttention-2技术进行训练

#### 🚄 基于PI和YaRN的超长上下文扩展技术

- 在[一期项目](https://github.com/ymcui/Chinese-LLaMA-Alpaca)中，我们实现了[基于NTK的上下文扩展技术](https://github.com/ymcui/Chinese-LLaMA-Alpaca/pull/743)，可在不继续训练模型的情况下支持更长的上下文
- 基于[位置插值PI](https://arxiv.org/abs/2306.15595)和NTK等方法推出了16K长上下文版模型，支持16K上下文，并可通过NTK方法最高扩展至24K-32K
- 基于[YaRN](https://arxiv.org/abs/2309.00071)方法进一步推出了64K长上下文版模型，支持64K上下文
- 进一步设计了**方便的自适应经验公式**，无需针对不同的上下文长度设置NTK超参，降低了使用难度

#### 🤖 简化的中英双语系统提示语

- 在[一期项目](https://github.com/ymcui/Chinese-LLaMA-Alpaca)中，中文Alpaca系列模型使用了[Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)的指令模板和系统提示语
- 初步实验发现，Llama-2-Chat系列模型的默认系统提示语未能带来统计显著的性能提升，且其内容过于冗长
- 本项目中的Alpaca-2系列模型简化了系统提示语，同时遵循Llama-2-Chat指令模板，以便更好地适配相关生态

## 模型下载

### 模型选择指引

以下是本项目的模型对比以及建议使用场景。**如需聊天交互，请选择Instruct版。**

| 对比项                | 中文Mixtral                                     | 中文Mixtral-Instruct                                  |
| :-------------------- | :----------------------------------------------------: | :----------------------------------------------------------: |
| 模型类型 | **基座模型** | **指令/Chat模型（类ChatGPT）** |
| 模型大小 | 8x7B（实际激活约13B） | 8x7B（实际激活约13B） |
| 训练类型     | Causal-LM (CLM)           | 指令精调                                                     |
| 训练方式 | QLoRA + 全量emb/lm-head | QLoRA + 全量emb/lm-head |
| 基于什么模型训练 | 原版Mixtral-8x7B-v0.1 | 中文Mixtral |
| 训练语料 | 无标注通用语料 | 有标注指令数据 |
| 词表大小 | 原版词表，32000 | 原版词表，32000 |
| 上下文长度 | 32K | 32K |
| 输入模板              | 不需要                                                 | 需要套用特定模板<sup>[3]</sup> |
| 适用场景            | 文本续写：给定上文，让模型生成下文            | 指令理解：问答、写作、聊天、交互等 |
| 不适用场景          | 指令理解 、多轮聊天等                                  |  文本无限制自由生成                                                       |


### 完整模型下载

以下是完整版模型，直接下载即可使用，无需其他合并步骤。推荐网络带宽充足的用户。同时提供了兼容llama.cpp等工具的GGUF量化版模型。

| 模型名称                  |   类型   | 大小 |                    下载地址                    |                    GGUF                    |
| :------------------------ | :------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| Chinese-Mixtral | 基座模型 | 94 GB | [百度] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral) | [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-gguf) |
| Chinese-Mixtral-Instruct | 指令模型 | 94 GB | [百度] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct) | [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct-gguf) |

### LoRA模型下载

以下是LoRA模型（含emb/lm-head），与上述完整模型一一对应。需要注意的是**LoRA模型无法直接使用**，必须按照教程与重构模型进行合并。推荐网络带宽不足，手头有原版Mixtral且需要轻量下载的用户。

| 模型名称                  |   类型   |                   合并所需基模型                   | 大小 |                    LoRA下载地址                    |
| :------------------------ | :------: | :--------------------------------------------------------: | :----------------: | :----------------------------------------------------------: |
| Chinese-Mixtral-LoRA | 基座模型 | [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) | 2.4 GB | [百度] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-lora) |
| Chinese-Mixtral-Instruct-LoRA | 指令模型 |        [Mixtral-8x7B-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)        | 2.4 GB | [百度] [[🤗HF]](https://huggingface.co/hfl/chinese-mixtral-instruct-lora) |

> [!IMPORTANT] 
> LoRA模型无法单独使用，必须与原版Mixtral-8x7B-v0.1进行合并才能转为完整模型。
>
> 合并模型方法：[link]


## 推理与部署

本项目中的相关模型主要支持以下量化、推理和部署方式，具体内容请参考对应教程。

| 工具   | 特点     | CPU  | GPU  | 量化 | GUI  | API  | vLLM<sup>§</sup> |                      教程                             |
| :----------------------------------------------------------- | ---------------------------- | :--: | :--: | :--: | :--: | :--: | :--: |:--: |
| [**llama.cpp**](https://github.com/ggerganov/llama.cpp)      | 丰富的量化选项和高效本地推理 |  ✅   |  ✅   |  ✅   |  ❌   |  ✅   |  ❌   | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/llamacpp_zh) |
| [**🤗Transformers**](https://github.com/huggingface/transformers) | 原生transformers推理接口     |  ✅   |  ✅   |  ✅   |  ✅   |  ❌   |  ✅  | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/inference_with_transformers_zh) |
| [**Colab Demo**](https://colab.research.google.com/drive/1yu0eZ3a66by8Zqm883LLtRQrguBAb9MR?usp=sharing) | 在Colab中启动交互界面 | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | [link](https://colab.research.google.com/drive/1yu0eZ3a66by8Zqm883LLtRQrguBAb9MR?usp=sharing) |
| [**仿OpenAI API调用**](https://platform.openai.com/docs/api-reference) | 仿OpenAI API接口的服务器Demo |  ✅   |  ✅   |  ✅   |  ❌   |  ✅   |  ✅  | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/api_calls_zh) |
| [**text-generation-webui**](https://github.com/oobabooga/text-generation-webui) | 前端Web UI界面的部署方式 |  ✅   |  ✅   |  ✅   |  ✅   |  ✅<sup>†</sup>  | ❌  | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/text-generation-webui_zh) |
| [**LangChain**](https://github.com/hwchase17/langchain) | 适合二次开发的大模型应用开源框架 |  ✅<sup>†</sup>  |  ✅   |  ✅<sup>†</sup>   |  ❌   |  ❌   | ❌  | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/langchain_zh) |
| [**privateGPT**](https://github.com/imartinez/privateGPT) | 多文档本地问答框架 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | [link](https://github.com/ymcui/Chinese-Mixtral/wiki/privategpt_zh) |

> [!NOTE]
> <sup>†</sup> 工具支持该特性，但教程中未实现，详细说明请参考对应官方文档<br/>
> <sup>‡</sup> 指是否支持长上下文版本模型（需要第三方库支持自定义RoPE）<br/>
> <sup>§</sup> vLLM后端不支持长上下文版本模型<br/>


## 系统效果

为了评测相关模型的效果，本项目分别进行了生成效果评测和客观效果评测（NLU类），从不同角度对大模型进行评估。需要注意的是，综合评估大模型能力仍然是亟待解决的重要课题，单个数据集的结果并不能综合评估模型性能。推荐用户在自己关注的任务上进行测试，选择适配相关任务的模型。

### 生成效果评测

为了更加直观地了解模型的生成效果，本项目仿照[Fastchat Chatbot Arena](https://chat.lmsys.org/?arena)推出了模型在线对战平台，可浏览和评测模型回复质量。对战平台提供了胜率、Elo评分等评测指标，并且可以查看两两模型的对战胜率等结果。题库来自于[一期项目人工制作的200题](https://github.com/ymcui/Chinese-LLaMA-Alpaca/tree/main/examples/f16-p7b-p13b-33b)，以及在此基础上额外增加的题目。生成回复具有随机性，受解码超参、随机种子等因素影响，因此相关评测并非绝对严谨，结果仅供晾晒参考，欢迎自行体验。部分生成样例请查看[examples目录](./examples)。

**⚔️ 模型竞技场：[http://llm-arena.ymcui.com](http://llm-arena.ymcui.com/)**

| 系统                                                         | 对战胜率（无平局） ↓ | Elo评分 |
| ------------------------------------------------------------ | :------------------: | :-----: |
| **Chinese-Mixtral-Instruct**                                 |                      |         |
| Chinese-Alpaca-2-13B-16K                                     |                      |         |
| Chinese-Alpaca-2-13B                                         |                      |         |
| [Chinese-Alpaca-Pro-33B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |                      |         |
| Chinese-Alpaca-2-7B                                          |                      |         |
| [Chinese-Alpaca-Pro-7B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |                      |         |
| Chinese-Alpaca-2-7B-16K                                      |                      |         |
| [Chinese-Alpaca-Pro-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |                      |         |


> [!NOTE]
> 以上结果截至2023年9月1日。最新结果请进入[**⚔️竞技场**](http://llm-arena.ymcui.com/)进行查看。

### 客观效果评测

#### C-Eval

[C-Eval](https://cevalbenchmark.com)是一个全面的中文基础模型评估套件，其中验证集和测试集分别包含1.3K和12.3K个选择题，涵盖52个学科。实验结果以“zero-shot / 5-shot”进行呈现。C-Eval推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/ceval_zh)

| Models             | Valid (0-shot) | Valid (5-shot) | Test (0-shot) | Test (5-shot) |
| ------------------------ | :------------: | :------------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct |                |                |               |               |
| Chinese-Mixtral          |                |                |               |               |


#### CMMLU

[CMMLU](https://github.com/haonan-li/CMMLU)是另一个综合性中文评测数据集，专门用于评估语言模型在中文语境下的知识和推理能力，涵盖了从基础学科到高级专业水平的67个主题，共计11.5K个选择题。CMMLU推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/cmmlu_zh)

| Models             | Valid (0-shot) | Valid (few-shot) | Test (0-shot) | Test (few-shot) |
| ------------------------ | :------------: | :------------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct |                |                |               |               |
| Chinese-Mixtral          |                |                |               |               |

#### MMLU

MMLU是一个用于评测自然语言理解能力的英文评测数据集，是当今用于评测大模型能力的主要数据集之一，其中验证集和测试集分别包含？和？个选择题，涵盖52个学科。MMLU推理代码请参考本项目：[📖GitHub Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/mmlu_zh)

| Models             | Valid (0-shot) | Valid (few-shot) | Test (0-shot) | Test (few-shot) |
| ------------------------ | :------------: | :------------: | :-----------: | :-----------: |
| Chinese-Mixtral-Instruct |                |                |               |               |
| Chinese-Mixtral          |                |                |               |               |

## 训练与精调

### 预训练

- 在原版Llama-2的基础上，利用大规模无标注数据进行增量训练，得到Chinese-LLaMA-2系列基座模型
- 训练数据采用了一期项目中Plus版本模型一致的数据，其总量约120G纯文本文件
- 训练代码参考了🤗transformers中的[run_clm.py](https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py)，使用方法见[📖预训练脚本Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/pt_scripts_zh)

### 指令精调

- 在Chinese-LLaMA-2的基础上，利用有标注指令数据进行进一步精调，得到Chinese-Alpaca-2系列模型
- 训练数据采用了一期项目中Pro版本模型使用的指令数据，其总量约500万条指令数据（相比一期略增加）
- 训练代码参考了[Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)项目中数据集处理的相关部分，使用方法见[📖指令精调脚本Wiki](https://github.com/ymcui/Chinese-Mixtral/wiki/sft_scripts_zh)

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
