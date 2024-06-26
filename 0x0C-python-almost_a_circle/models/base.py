#!/usr/bin/python3
"""
Base class definition
"""
import json
import csv


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

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Return: a list of instances
        """

        name = cls.__name__
        name += '.json'

        li = []
        li2 = []
        try:
            with open(name, 'r') as f:
                li = cls.from_json_string(f.read())
            for i in li:
                li2.append(cls.create(**i))
            return li2
        except IOError:
            return li2

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Return: a list of instances
        """

        name = cls.__name__
        name += '.csv'

        with open(name, 'w') as f:
            if list_objs is None or list_objs == []:
                csv.write('[]')
            elif cls.__name__ == 'Rectangle':
                hedername = ['id', 'width', 'height', 'x', 'y']
            else:
                hedername = ['id', 'size', 'x', 'y']

            writer = csv.DictWriter(f, hedername)

            for i in list_objs:
                writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return: a list of instances
        """

        name = cls.__name__
        name += '.csv'

        try:
            with open(name, 'r') as f:
                if cls.__name__ == 'Rectangle':
                    hedername = ['id', 'width', 'height', 'x', 'y']
                else:
                    hedername = ['id', 'size', 'x', 'y']
                read = csv.DictReader(f, hedername)
                li = []
                for x in read:
                    for i, n in x.items():
                        x[i] = int(n)
                    li.append(x)
                return ([cls.create(**i) for i in li])

        except FileNotFoundError:
            return []
