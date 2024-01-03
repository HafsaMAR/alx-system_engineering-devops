#!/usr/bin/python3
""" TAsk0 model """

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

    def todo_true(list):
        n = 0
        for dic in list:
            if dic.get("completed"):
                n += 1
        return (n)

    tr = todo_true(data_todo)
    name = data_user[0].get("name")

    output = f"Employee {name} is done with tasks({tr}/{len(data_todo)}):"
    print(output)

    for dic in data_todo:
        if dic.get("completed"):
            print(f" \t{dic.get('title')}")
