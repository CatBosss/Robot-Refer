from mcap.reader import make_reader
import os

mcap_file = "./my_training_data/Cooking_and_Kitchen_Clean/clean_bowl/00001/00001.mcap"

if not os.path.exists(mcap_file):
    print("文件未找到，请检查路径！")
    exit()

print(f"正在分析文件: {mcap_file} ...")

# 存储我们找到的所有 Topics
found_topics = set()

with open(mcap_file, "rb") as f:
    reader = make_reader(f)
    
    # 遍历消息，从消息关联的 channel 中获取 topic
    # iter_messages 会返回 (schema, channel, message)
    for schema, channel, message in reader.iter_messages():
        found_topics.add(channel.topic)
        
        # 为了演示，只读前 100 条消息就停，防止文件过大导致无限循环
        if len(found_topics) > 50: # 这里只是为了测试，实际上如果你想看完全部，可以把这个限制去掉
            break

print("\n--- 在文件中发现的 Topic ---")
for topic in sorted(found_topics):
    print(f"Topic: {topic}")

print("\n文件解析测试成功！")