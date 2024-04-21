#!/usr/bin/python3
"""
Rectangle class definition
"""
from models.base import Base


class Rectangle(Base):
    """
    full Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: a number
            y: a number
            id: a number
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Returns: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, val):
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
    
        self.__width = val

    @property
    def height(self):
        """
            Returns: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Args:
            val: the new height of rectangle
        Raises:
            TypeError: If height is not an int
            ValueError: If height is under or equal to 0
        """
        if type(val) is not int:
             raise TypeError('height must be an integer')
        elif val <= 0:
             raise ValueError('height must be > 0')
    
        self.__height = val

    @property
    def x(self):
        """
            Returns: x of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Args:
            val: the new x of rectangle
        Raises:
            TypeError: If x is not an int
            ValueError: If x is under 0
        """
        if type(val) is not int:
             raise TypeError('x must be an integer')
        elif val < 0:
             raise ValueError('x must be >= 0')
    
        self.__x = val

    @property
    def y(self):
        """
            Returns: y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Args:
            val: the new y of rectangle
        Raises:
            TypeError: If y is not an int
            ValueError: If y is under 0
        """
        if type(val) is not int:
             raise TypeError('y must be an integer')
        elif val < 0:
             raise ValueError('y must be >= 0')
    
        self.__y = val

    def area(self):
        """
            Returns: the area of the rectangle
        """

        return (self.width * self.height)

    def display(self):
        """
            print: the rectangle
        """

        for y1 in range(self.__y):
            for x1 in range(self.__x):
                print('#')

        #print(['#' for ])
