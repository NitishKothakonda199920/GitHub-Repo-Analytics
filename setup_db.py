import sqlite3

conn = sqlite3.connect("github_repos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS repositories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    repo_name TEXT,
    stars INTEGER,
    forks INTEGER,
    commits INTEGER
)
""")

conn.commit()
conn.close()