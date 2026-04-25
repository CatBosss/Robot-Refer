# GenRobot AI

## 简介

一家专门做具身智能（Embodied AI）数据基础设施的平台公司。
官网：https://www.genrobot.ai/

### 核心模式

给所有机器人公司“卖铲子”

- 硬件层：
	DAS Gripper：双指夹爪，采集机器人训练数据
	DAS Ego：第一视角采集系统
	
- 数据资产：10Kh RealOmni-Open Dataset
	https://huggingface.co/datasets/genrobot2025/10Kh-RealOmin-OpenData
	
- 平台层：Gen Matrix
	从采集 → 清洗 → 标注 → 模型评估 全流程自动化
	
- 服务层：Custom Dataset Services

## Huggingface 大数据集 处理方案：10Kh-RealOmin-OpenData

核心原则是：**不要本地化所有数据，而是将其视为一个“流式数据源”来处理。**

### 阶段0：环境配置与工具准备

**安装 Hugging Face 工具：** 需要 `huggingface_hub` 来进行筛选和下载。

```
pip install huggingface_hub
```

**利用官方数据工具包 das-datakit：** 处理 MCAP 文件的核心。
https://github.com/genrobot-ai/das-datakit

```
git clone https://github.com/genrobot-ai/das-datakit
cd das-datakit
pip install -r requirements.txt
```

### 阶段一：建立元数据索引 (Indexing)

**目的：** 避免全量下载，建立本地“数据地图”。使用 SQLite 数据库存储整个数据集的目录结构。

**操作：** 运行仓库目录下的 `indexing.py`。
**产出：** `dataset.db`。它是一个轻量级数据库，包含所有文件的元数据路径。

### 阶段二：数据筛选与定向下载 (Filtering & Download)

**目的：** 根据训练任务需求，只提取目标子集所需的 MCAP 文件。（如“厨房整理”）

**操作：** 使用 `get_task.py` 脚本，查询数据集中有哪些任务。
结果如下：
```
                                    task   count
0               Clutter Tidy-Up [Stage2]   13000
1              Cooking_and_Kitchen_Clean    1912
2  Folding_Clothes_and_Zipper_Operations   36556
3                       Organize_Clutter   26704
4                         Shoes_Handling     731
5                              [STAGE 3]  589087

```


**操作：** 使用 `download_task.py` 脚本，根据 SQL 条件筛选数据集并下载mcap文件。


### 阶段三：mcap文件查看或解析

**视觉化直观查看**
下载的文件，比如“00001.mcap”，可以通过以下网址，视觉化直观查看。将mcap文件拖入指定区域即可。
https://monitor.genrobot.com/#/index

**代码级读取**，解析文件，比如“00001.mcap”，
**操作：** 使用 `inspect_mcap.py` 脚本，分析mcap

```
pip install mcap
python3 inspect_mcap.py
```

结果如下：
```
正在分析文件: ./my_training_data/Cooking_and_Kitchen_Clean/clean_bowl/00001/00001.mcap ...

--- 在文件中发现的 Topic ---
Topic: /robot0/sensor/camera0/camera_info
Topic: /robot0/sensor/camera0/compressed
Topic: /robot0/sensor/imu
Topic: /robot0/sensor/magnetic_encoder
Topic: /robot0/sim/robot_info
Topic: /robot0/system_info
Topic: /robot0/vio/eef_pose
Topic: /robot1/sensor/camera0/camera_info
Topic: /robot1/sensor/camera0/compressed
Topic: /robot1/sensor/imu
Topic: /robot1/sensor/magnetic_encoder
Topic: /robot1/sim/robot_info
Topic: /robot1/system_info
Topic: /robot1/vio/eef_pose

文件解析测试成功！
```


