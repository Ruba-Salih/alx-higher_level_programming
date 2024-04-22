#!/usr/bin/python3
"""
Square class definition
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    full Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size: size of the Square
            x: a number
            y: a number
            id: a number
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            print: the Square attributes
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
            Returns: size of the Square
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Args:
            val: the new width of rectangle
        Raises:
            TypeError: If width is not an int
            ValueError: If width is under or equal to 0
        """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')

        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        Args:
            args: numbers of values
            kwargs: numbers of values in dic structur
        """

        if len(args) != 0 and not None:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
        else:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """
        Rerturns: dictionary
        """

        dict = {}
        dict['id'] = self.id
        dict['size'] = self.size
        dict['x'] = self.x
        dict['y'] = self.y

        return dict
