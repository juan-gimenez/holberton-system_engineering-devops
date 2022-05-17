#!/usr/bin/python3
"""
script to export data in the CSV format.
"""


import csv
import requests
import sys

if __name__ == "__main":
    usr = argv[1]

    us_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(usr)
    t_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(usr)

    r_todo = requests.get(t_url).json()
    r_user = requests.get(us_url).json()

    with open("{}.csv".format(usr), newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in r_todo:
            writer.writerow([int(usr),r_user.get('username'),
                             task.get('completed'),
                             task.get('title')])
