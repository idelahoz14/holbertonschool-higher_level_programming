#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """
import urllib.request
import sys
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            print(f.read().decode("utf-8"))
    except HTTPError as exception:
        print('Error code: {}'.format(exception.code))
