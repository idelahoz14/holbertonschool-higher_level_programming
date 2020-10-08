#!/usr/bin/python3
"""Represent a Student"""


class Student:
    """Represent Student class"""
    def __init__(self, first_name, last_name, age):
        """Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to json"""

        if attrs is None:
            return (self.__dict__)

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
