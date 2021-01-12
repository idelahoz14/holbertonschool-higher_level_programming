#!/usr/bin/python3
""" script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter. """
import requests
from sys import argv

if __name__ == "__main__":
    x = argv[1] if len(argv) > 1 else ""
    try:
        r = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': x}).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
