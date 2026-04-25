import sqlite3
import os
import pandas as pd  # 【关键点：一定要有这一行】
from huggingface_hub import hf_hub_download

# 1. 确保数据库路径正确
db_path = os.path.join(os.path.dirname(__file__), 'dataset.db')
conn = sqlite3.connect(db_path)

print("正在从数据库筛选数据...")

# 2. 查询数据
# 注意：这里确保表名是 files，任务名拼写和你数据库里的一致
query = "SELECT fullpath FROM files WHERE task = 'Cooking_and_Kitchen_Clean' LIMIT 5"
rows = pd.read_sql_query(query, conn)

# 3. 设置下载保存路径
repo_id = "genrobot2025/10Kh-RealOmin-OpenData"
save_dir = os.path.join(os.path.dirname(__file__), 'my_training_data')
os.makedirs(save_dir, exist_ok=True)

# 4. 循环下载
print(f"准备下载 {len(rows)} 个文件至: {save_dir}")

for index, row in rows.iterrows():
    path = row['fullpath']
    print(f"正在下载: {path}")
    hf_hub_download(
        repo_id=repo_id,
        filename=path,
        repo_type="dataset",
        local_dir=save_dir,
        local_dir_use_symlinks=False # 建议设为 False 以免生成链接文件
    )

conn.close()
print("下载完成！")