#!/usr/bin/python3
"""Square class"""


class Square:
    """Represent a square
    Arguments:
        size: size of a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of a square"""
        return self.__size ** 2
