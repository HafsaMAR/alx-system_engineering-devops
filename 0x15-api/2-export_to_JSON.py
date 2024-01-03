#!/usr/bin/python3
"""Task2 dump data into json"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    # task 0 function
    id = argv[1]
    params_todo = {"userId": id}
    params_user = {"id": id}
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_user = "https://jsonplaceholder.typicode.com/users"

    response_todo = requests.get(url_todo, params=params_todo)
    data_todo = response_todo.json()
    response_user = requests.get(url_user, params=params_user)
    data_user = response_user.json()

    username = data_user[0].get("username")
    """Task2"""
    list_todo = []

    for dic in data_todo:
        task = dic.get("title")
        completed = dic.get("completed")
        td = {"task": task, "completed": completed, "username": username}
        list_todo.append(td)

    output = {id: list_todo}

    # Specify the file path
    file_path = '{}.json'.format(id)

    with open(file_path, 'w') as json_file:

        json.dump(output, json_file, indent=2)
