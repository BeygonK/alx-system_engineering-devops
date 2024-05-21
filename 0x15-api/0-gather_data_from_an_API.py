#!/usr/bin/python3
"""Python script that, using this REST API,
    for a given employee ID, 
    returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(user_id):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(user_id) and task.get('completed')]))
