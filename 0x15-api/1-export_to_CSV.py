#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv
import csv


def API_request(argv):
    """Gather data from an API and past it to csv"""
    todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])

    responset = requests.get(todo)
    responseu = requests.get(users)
    json_t = responset.json()
    json_u = responseu.json()
    user_name = json_u.get("username")

    with open(str(argv[1])+"."+"csv", 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for count in json_t:
            writer.writerow([str(argv[1]), str(user_name),
                            str(count['completed']), str(count['title'])])


if __name__ == "__main__":
    API_request(argv)
