#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
from sys import argv


def API_request(argv):
    """Gather data from an API and past it to csv"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("username")

    dic_complete = {}
    list_json = []
    for i in json_t:
        my_dic = {'task': '', 'completed': None, 'username': user_name}
        task_title = i.get('title')
        true_false = i.get('completed')
        my_dic.update(task=task_title, completed=true_false)
        list_json.append(my_dic)
    dic_complete.update({argv[1]: list_json})

    with open(argv[1]+"."+"json", 'w') as file:
        json.dump(dic_complete, file)


if __name__ == "__main__":
    API_request(argv)
