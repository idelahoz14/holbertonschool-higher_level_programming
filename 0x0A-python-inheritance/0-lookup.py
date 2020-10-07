#!/usr/bin/python3
"""function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """dir(obj)
    Arguments:
        obj (any) -- [type of object]
    Returns:
        [dir(obj)] -- attributes and methods of an obj
    """
    return dir(obj)
