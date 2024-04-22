#!/usr/bin/python3
"""
Base class definition
"""
import json


class Base:
    """
    Base class with private instance attribute __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id: a number
        """

        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries:  a list of dictionaries
        Returns: the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Args:
            list_objs:  is a list of instances who inherits of Base
        """

        name = cls.__name__
        name += '.json'

        li = []
        if list_objs is not None:
            for i in list_objs:
                li.append(cls.to_dictionary(i))

        with open(name, 'w') as f:
            f.write(cls.to_json_string(li))
