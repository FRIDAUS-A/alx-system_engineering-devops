#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list
progress.
"""

import csv
import json
import requests
import sys
if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    task = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    Id = response.json()["id"]
    username = response.json()["username"]
    total_task = requests.get(task, params={"userId": Id})
    task_done = requests.get(task, params={"userId": Id, "completed": "true"})

    csv_file = f"{Id}.csv"
    count = False
    with open(csv_file, 'w') as csvfile:
        for json_data in total_task.json():
            json_data['UserId'] = username
            json_data['id'] = Id
            if count not True:
                header = ['UserId', 'id', 'completed', 'title']
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                count = True
            filtered_data = {key: f"'{json_data[key]}'" for key in header}
            writer.writerow(filtered_data)
