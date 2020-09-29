#!/usr/bin/python3
"""Represent a rectangle"""


class Rectangle:
    """Represent a rectangle"""

    # count instances
    number_of_instances = 0
    # symbol
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialization of rectangle class
        Keyword Arguments:
            width (int) -- width of the rectangle (default: (0))
            height (int) -- height of the rectangle (default: (0))

        Raises:
            TypeError: if the values are not integers
            ValueError: if the value is negative
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width property
        Returns:
            (int) -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Arguments:
            value (int) -- represent the width of the rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property
        Returns:
            (int) -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Arguments:
            value (int) -- height of the rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle
        Returns:
            (int) -- area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """perimeter of the rectangle
        Returns:
            (int) -- perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.height + 2 * self.width

    def __str__(self):
        """str method
        Returns:
            (str) -- print rectangle in #
        """
        str = ""
        if self.width == 0 or self.height == 0:
            return str
        for i in range(0, self.height):
            str += '#' * self.width
            if i != self.height - 1:
                str += '\n'
        return str

    def __repr__(self):
        """repr method
        Returns:
            (str) -- rectangle properties
        """
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """destructor method
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
