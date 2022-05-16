#!/usr/bin/python3
"""returns information about his/her TODO list progress"""


if __name__ == '__main__':
    import requests
    from sys import argv

    rtodos = requests.get('https://jsonplaceholder.typicode.com/todos')
    rusers = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_to_json = rtodos.json()
    users_to_json = rusers.json()
    name = users_to_json[int(argv[1]) - 1]['name']
    emp_id = int(argv[1])
    l = []
    for i in todos_to_json:
        if i['userId'] == emp_id:
            if i['completed'] is True:
                done += 1
                done.append(i['title'])
            task += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name, done, task))
    for TASK_TITLE in l:
        print('\t {}'.format(TASK_TITLE))
