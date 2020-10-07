#!/usr/bin/python3
"""function that create an object from a json file"""
import json


def load_from_json_file(filename):
    """create an object from json file"""

    with open(filename) as reader:
        return json.load(reader)
