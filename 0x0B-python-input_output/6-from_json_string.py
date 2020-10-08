#!/usr/bin/python3
"""representation of object to json"""
import json


def from_json_string(my_str):
    """object to json"""

    return json.loads(my_str)
