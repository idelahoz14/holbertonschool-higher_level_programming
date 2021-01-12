#!/usr/bin/python3
""" script that takes your Github credentials
(username and password) and uses the Github API
to display your id """
import requests
from sys import argv


if __name__ == "__main__":
    information = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in information:
        print(information['id'])
    else:
        print(None)
