#!/bin/env python3
import datetime
import subprocess
import os
import random
import string

strings = string.ascii_letters + string.digits

GIT_COMMAND = ["git", "commit", "-am", "Auto Commit"]

my_env = os.environ.copy()
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(35)]


for i in date_list:
    author_date = i.strftime("%Y-%m-%d %H:%M")
    my_env["GIT_AUTHOR_DATE"] = author_date
    my_env["GIT_COMMITTER_DATE"] = author_date

    # Generate a random number of commits
    num_of_commits = random.randrange(0, 7)
    print(f"Date: {author_date}, Commits: {num_of_commits}")
    for _ in range(num_of_commits):
        with open("file.txt", "w") as f:
            text = "".join([random.choice(strings) for _ in range(20)]) + "\n"
            f.write(text)
        subprocess.Popen(GIT_COMMAND, env=my_env).wait(20)
