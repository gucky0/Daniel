import os
repo = os.getcwd()
os.chdir(repo)

commit_message = "web scraping - anime"


line2 = "git init"
line3 = "git status"
line4 = "git add -A"
line5 = f'git commit -m "{commit_message}"'
line6 = "git remote add origin https://github.com/gucky0/Star"
line7 = "git remote -v"
line8 = "git push -f origin main"

def osu(line):
    os.system(line + " & pause")

lines = [var for var in dir() if not var.startswith("__") and var not in ("os", "osu", "repo", "commit_message")]

for line in lines:
    osu(locals()[line])

