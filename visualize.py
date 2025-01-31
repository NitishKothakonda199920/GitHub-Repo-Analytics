import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load data from SQLite
conn = sqlite3.connect("github_repos.db")
df = pd.read_sql_query("SELECT * FROM repositories", conn)
conn.close()

# Plot bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["repo_name"], df["stars"], color="blue", label="Stars")
plt.bar(df["repo_name"], df["forks"], color="green", bottom=df["stars"], label="Forks")
plt.xlabel("Repository")
plt.ylabel("Count")
plt.title("GitHub Repository Statistics")
plt.legend()
plt.show()
