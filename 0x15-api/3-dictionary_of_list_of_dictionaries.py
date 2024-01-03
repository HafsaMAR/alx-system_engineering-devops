#!/usr/bin/python3
""" whole data dumping into json file"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users"
    all_users = requests.get(url_user).json()
    user_dictionnary = {}
    for user in all_users:
        list_user = []
        id = user.get("id")
        url_todo = "https://jsonplaceholder.typicode.com/todos"
        data_todo = requests.get(url_todo, params={"userId": id}).json()
        username = user.get("username")
        for dic in data_todo:
            task = dic.get("title")
            completed = dic.get("completed")
            td = {"username": username, "task": task, "completed": completed}
            list_user.append(td)
        user_dictionnary[id] = list_user

    file_path = 'todo_all_employees.json'
    with open(file_path, 'w') as json_file:
        json.dump(user_dictionnary, json_file)
