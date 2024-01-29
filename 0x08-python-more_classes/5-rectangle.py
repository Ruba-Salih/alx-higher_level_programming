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
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Args:
            value: value
        """
        if self.check_val(value, 0):
            self.__width = value

    @property
    def height(self):
        """
        return height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Args:
            value: value
        """
        if self.check_val(value, 1):
            self.__height = value

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

    def area(self):
        """
        return area
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        return perimeter
        """
        if self.width == 0 or self.height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        return string
        """
        if self.width == 0 or self.height == 0:
            return ('')

        rg = '#' * self.width
        rg2 = rg
        for i in range(self.height):
            rg += '\n' + rg
        return (rg)

    def __repr__(self):
        """
        return string
        """
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """
        delet rectangle instainc
        """
        print('Bye rectangle...')
