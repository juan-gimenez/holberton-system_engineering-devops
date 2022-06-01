#!/usr/bin/python3
""" Export data in the CSV format"""
import json
import requests
import sys


if __name__ == "__main__":
    r = requests.get("https://jsonplaceholder.typicode.com/users/" +
                     sys.argv[1])
    dict1 = json.loads(r.text)
    usr = dict1.get('username')
    r = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                     "?userId=" + sys.argv[1])
    everyone = json.loads(r.text)
    tasks = [task for task in everyone]
    answ = {sys.argv[1]: []}
    for task in tasks:
        dict2 = {"task": task.get('title'),
                 'completed': task.get('completed'), 'username': usr}
        answ.get(sys.argv[1]).append(dict2)
    with open(sys.argv[1] + ".json", "w") as f:
        json.dump(answ, f)
