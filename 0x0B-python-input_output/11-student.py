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

    def to_json(self):
        """function to json"""

        return (self.__dict__)
