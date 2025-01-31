import requests # type: ignore
import sqlite3

# GitHub repository details
GITHUB_OWNER = "octocat"
REPO_NAME = "Hello-World"

# Fetch repository details
url = f"https://api.github.com/repos/{GITHUB_OWNER}/{REPO_NAME}"
response = requests.get(url)
repo_data = response.json()

stars = repo_data.get("stargazers_count", 0)
forks = repo_data.get("forks_count", 0)

# Fetch commit count
commits_url = f"https://api.github.com/repos/{GITHUB_OWNER}/{REPO_NAME}/commits"
commits_response = requests.get(commits_url)
commits = len(commits_response.json())

# Store in SQLite
conn = sqlite3.connect("github_repos.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO repositories (repo_name, stars, forks, commits) VALUES (?, ?, ?, ?)", 
               (REPO_NAME, stars, forks, commits))

conn.commit()
conn.close()

print(f"Data for {REPO_NAME} inserted successfully!")