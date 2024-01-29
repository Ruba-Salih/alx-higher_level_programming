#!/usr/bin/python3
"""
Rectangle class definition
"""


class Rectangle:
    """
    full Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        return width
        """
        return (self.width)

    @width.setter
    def width(self, value):
        """
        Args:
            value: value
        """
        if self.check_val(value, 0):
            self.width = value

    @property
    def height(self):
        """
        return height
        """
        return (self.height)

    @height.setter
    def height(self, value):
        """
        Args:
            value: value
        """
        if self.check_val(value, 1):
            self.height = value

    def check_val(self, val, flag):
        """
        Args:
            val: val
            flag: flag
        return True
        """
        if flag == 0:
            if type(val) is not int:
                raise TypeError('width must be an integer')
            elif val < 0:
                raise ValueError('width must be >= 0')
            else:
                return (True)
        else:
            if type(val) is not int:
                raise TypeError('height must be an integer')
            elif val < 0:
                raise ValueError('height must be >= 0')
            else:
                return (True)
