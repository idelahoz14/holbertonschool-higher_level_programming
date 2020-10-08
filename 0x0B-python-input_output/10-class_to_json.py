#!/usr/bin/python3
"""Returns the dictionary description
with simple data structure"""
import json


def class_to_json(obj):
    """returns the dictionary description"""

    return obj.__dict__
