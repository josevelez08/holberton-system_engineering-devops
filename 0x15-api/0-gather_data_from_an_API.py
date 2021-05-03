#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv
import json


def API_request(argv):
    """Gather data from an API"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("name")
    var1 = 0
    var2 = 0
    count = 0
    list1 = []
    for tasks in json_t:
        var1 += 1
        if tasks['completed'] is True:
            list1 += [tasks['title']]
            var2 += 2
    print("Employee {} is done with tasks({}/{}):".format(user_name, var2, var1))

    for count in list1:
        print('\t', str(count))


if __name__ == "__main__":
    API_request(argv)
