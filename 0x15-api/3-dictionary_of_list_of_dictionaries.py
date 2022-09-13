#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
            taskList = []
            for task in todos:
                if task.get('userId') == user.get('id'):
                    taskDict = {"username": user.get('username'),
                                "task": task.get('title'),
                                "completed": task.get('completed')}
                    taskList.append(taskDict)
            todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
