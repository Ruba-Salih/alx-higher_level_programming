#!/usr/bin/python3
"""
Base class definition
"""


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
