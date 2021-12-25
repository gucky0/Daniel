import os
repo = os.getcwd()

destination = "Daniel"

commit_message = "Updated VBA Lesson"
os.chdir(repo)

lines = [f"cd {repo}",
         "git init",
         "git status",
         "git remote remove origin",
         f"git remote add origin https://github.com/gucky0/{destination}",
         "git remote -v",
         "git pull origin main",
         "git add --all",
         "git status",
         f'git commit -m "{commit_message}"',
         "git show-ref",
         "git push origin main"]

def osu(line):
    os.system(line + " & pause")

##lines = [var for var in dir() if not var.startswith("__") and var not in ("os", "osu", "repo", "commit_message")]

for line in lines:
    osu(line)

