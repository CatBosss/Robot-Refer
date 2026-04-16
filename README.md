# Robot-Refer
这些链接涵盖了机器人的开源生态，以及最新的大模型驱动的机器人运动生成研究。不定期更新。

如果关注**人形机器人开发**，重点看 **GR00T** 和 **Unitree**；
如果关注**数据生成与大模型训练**，重点看 **MotionMillion** 和 NVIDIA 的 **synthetic-manipulation** 项目。

以下是各链接的简要说明：

### 1. NVIDIA 机器人与仿真平台

- **[synthetic-manipulation-motion-generation](https://github.com/NVIDIA-Omniverse-blueprints/synthetic-manipulation-motion-generation)**:
    
    这是 NVIDIA 基于 Omniverse 的蓝图项目，主要用于生成合成的**机械臂抓取和运动数据**。它利用仿真环境产生大量高质量标签数据，解决机器人训练中真实数据匮乏的问题。
    
- **[NVIDIA Explore / Discover](https://build.nvidia.com/explore/discover)**:
    
    NVIDIA 的云端服务平台，允许开发者在浏览器中直接体验和测试各种 **NVIDIA 微服务 (NIM)**，包括视觉 AI、语言模型和物理仿真等加速计算功能。
    
- **[Robot Learning Use Cases](https://www.nvidia.com/en-us/use-cases/robot-learning/)**:
    
    NVIDIA 机器人学习（Robot Learning）的官方案例页，展示了如何结合**强化学习、模仿学习**和 Isaac Sim 仿真环境来提升机器人的感知与操作能力。
    
- **[Project GR00T](https://developer.nvidia.com/isaac/gr00t)**:
    
    这是 NVIDIA 推出的专为**人形机器人**设计的多模态通用基础模型。它让机器人能够理解自然语言、观察人类动作并进行模仿，是 NVIDIA 进军通用机器人大脑的核心项目。
    
- **[NVIDIA Open Source Projects](https://developer.nvidia.com/open-source)**:
    
    NVIDIA 的开源项目索引页，汇集了其在 AI、GPU 加速计算、仿真等领域的开源工具和库，方便开发者按标题搜索和获取。
    

### 2. 宇树科技 (Unitree) 资源

- **[Unitree GitHub](https://github.com/unitreerobotics)**:
    
    宇树科技的官方代码仓库，包含了其四足机器人（如 Go2, B2）和人形机器人（如 H1, G1）的 **SDK、通信接口和底层控制算法**。
    
- **[Unitree Hugging Face](https://huggingface.co/unitreerobotics)**:
    
    宇树在 Hugging Face 上的空间，主要用于发布与机器人相关的**预训练模型权重和数据集**，支持基于 AI 的机器人运动控制研究。
    

### 3. ABot 操纵系统

- **[ABot-Manipulation](https://github.com/amap-cvlab/ABot-Manipulation)**:
    
    来自上海交通大学 AMAP 实验室的项目，专注于**机器人操纵（Manipulation）**。它通常涉及端到端的视觉决策，让机器人能够通过视觉输入完成复杂的物体抓取和放置任务。
    

### 4. MotionMillion (百万级运动生成研究)

- **[Go to Zero (GitHub)](https://github.com/VankouF/MotionMillion-Codes)**:
    
    这是一项关于**零样本（Zero-shot）运动生成**的研究成果。它通过大规模数据预训练，使机器人能够在未见过的场景下生成平滑且符合物理规律的动作。
    
- **[MotionMillion Dataset (Hugging Face)](https://huggingface.co/datasets/InternRobotics/MotionMillion)**:
    
    由 InternRobotics 发布的**百万级机器人运动数据集**。这是目前业内领先的大规模数据集，涵盖了丰富的动作序列，旨在支持开发如同 GPT 之于文字一样的“机器人动作大模型”。
    
