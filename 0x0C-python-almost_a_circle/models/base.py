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

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string:  is a string representing a list of dictionaries
        """
        li = []
        if json_string is not None and len(json_string) != 0:
            li = json.loads(json_string)
        return li

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            dictionary:  a dictionary
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                obj = cls(1, 1)
            else:
                obj = cls(1)

        return obj.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """
        Return: a list of instances
        """

        name = cls.__name__
        name += '.json'

        li = []
        try:
            with open(name, 'r') as f:
                li = cls.from_json_string(f.read(name))
                for i in range(len(li)):
                    li[i] = cls.create(**li[i])
        except ():
            pass
        return li
