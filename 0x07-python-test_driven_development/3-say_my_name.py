#!/usr/bin/python3
"""say_my_name function"""


def say_my_name(first_name, last_name=""):
    """This function print the first name and last name passed in
    Args:
        first_name (str): the first name
        last_name (str, optional): the last name
    Raises:
        TypeError: if the first_name or last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
