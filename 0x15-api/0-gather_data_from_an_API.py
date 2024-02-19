#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list
progress.
"""

import requests
import sys
url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
task = f"https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)

Id = response.json()["id"]
name = response.json()["name"]
total_task = requests.get(task, params={"user_id": Id})
task_done = requests.get(task, params={"user_id": Id, "completed": "true"})
print(f"Employee {name} is done with tasks({len(task_done.json())}/\
{len(total_task.json())}):")
for mem in task_done.json():
    print(f"\t{mem['title']}")
