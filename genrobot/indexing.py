import sqlite3
from huggingface_hub import HfApi

def scan_to_sqlite_improved():
    repo_id = "genrobot2025/10Kh-RealOmin-OpenData"
    db_name = "dataset1.db"
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # 初始化表
    cursor.execute('DROP TABLE IF EXISTS files')
    cursor.execute('''
        CREATE TABLE files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            skill TEXT,
            filename TEXT,
            fullpath TEXT
        )
    ''')
    conn.commit() # 立即提交表结构
    
    api = HfApi()
    print("正在连接服务器...")
    
    repo_files = api.list_repo_tree(repo_id=repo_id, repo_type="dataset", recursive=True)
    
    batch = []
    count = 0
    
    for item in repo_files:
        if item.path.endswith('.mcap'):
            parts = item.path.split('/')
            if len(parts) >= 3:
                batch.append((parts[0], parts[1], parts[2], item.path))
                count += 1
                
                # 每 5000 条插入并提交一次
                if len(batch) >= 5000:
                    cursor.executemany('INSERT INTO files (task, skill, filename, fullpath) VALUES (?,?,?,?)', batch)
                    conn.commit() # 【关键修改】每次批处理后立即保存到硬盘
                    batch = []
                    print(f"已成功索引并保存 {count} 个文件...")

    # 插入剩余
    if batch:
        cursor.executemany('INSERT INTO files (task, skill, filename, fullpath) VALUES (?,?,?,?)', batch)
        conn.commit()

    # 最后创建索引
    print("正在建立检索索引，这会提升后续查询速度...")
    cursor.execute('CREATE INDEX idx_task ON files(task)')
    cursor.execute('CREATE INDEX idx_skill ON files(skill)')
    conn.commit()
    conn.close()
    print(f"完成！总共存储了 {count} 条数据。")

scan_to_sqlite_improved()