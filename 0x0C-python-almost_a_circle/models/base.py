#!/usr/bin/python3
"""Base class"""
import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of dictionaries"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to json file"""
        jsonfile = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for i in list_objs:
                list_objects.append(cls.to_dictionary(i))
        with open(jsonfile, 'w') as reader:
            reader.write(cls.to_json_string(list_objects))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
