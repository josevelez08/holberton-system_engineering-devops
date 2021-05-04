#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv
import json


def API_request():
    """Gather data from an API"""
    user = "https://jsonplaceholder.typicode.com/todos/"
    var = 1

    for count in user:
        todo = "https://jsonplaceholder.typicode.com/todos/?userId=" + str(var)
        user1 = "https://jsonplaceholder.typicode.com/users/" + str(var)
        responseu = requests.get(user1)
        json_u = responseu.json()
        user_name = json_u.get("username")
        responset = requests.get(todo)
        json_t = responset.json()
        dic_complete = {}
        list_json = []
        if (user_name is None):
            return
        for i in json_t:
            my_dic = {'username': user_name, 'task': '', 'completed': None}
            task_title = i.get('title')
            true_false = i.get('completed')
            my_dic.update(task=task_title, completed=true_false)
            list_json.append(my_dic)
        dic_complete.update({str(var): list_json})
        with open("todo_all_employees.json", "a") as file:
            json.dump(dic_complete, file)
        print(dic_complete)
        var = var + 1


if __name__ == "__main__":
    API_request()
