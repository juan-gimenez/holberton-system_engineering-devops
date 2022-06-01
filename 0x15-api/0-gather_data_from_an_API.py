#!/usr/bin/python3
"""returns information about his/her TODO list progress"""


if __name__ == '__main__':
    import requests
    from sys import argv

    rtodos = requests.get('https://jsonplaceholder.typicode.com/todos')
    rusers = requests.get('https://jsonplaceholder.typicode.com/users')

    todos_to_json = rtodos.json()
    users_to_json = rusers.json()

    emp_id = int(argv[1])
    name = users_to_json[int(argv[1]) - 1]['name']
    task = 0
    done = 0
    list_titles = []
    for i in todos_to_json:
        if i['userId'] == emp_id:
            if i['completed'] is True:
                done += 1
                list_titles.append(i['title'])
            task += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        name, done, task))
    for TASK_TITLE in list_titles:
        print('\t {}'.format(TASK_TITLE))
