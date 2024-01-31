#!/usr/bin/python3
"""
Rectangle class definition
"""


class Rectangle:
    """
    full Rectangle class
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        rg = ('{}'.format(self.print_symbol) * self.width)
        rg2 = rg
        for i in range(self.height - 1):
            rg2 += '\n' + rg
        return (rg2)

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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
         returns the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
         returns a new Rectangle instance
        """
        return (Rectangle(size, size))