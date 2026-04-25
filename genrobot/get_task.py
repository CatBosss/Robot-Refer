import sqlite3
import pandas as pd

conn = sqlite3.connect('dataset.db')
# 查看有哪些任务类别
df_tasks = pd.read_sql_query("SELECT task, COUNT(*) as count FROM files GROUP BY task", conn)
print("你当前拥有的任务分布情况：")
print(df_tasks)
conn.close()
