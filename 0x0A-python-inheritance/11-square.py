#!/usr/bin/python3
"""Defines a class Square based on 9-rectangle.py

Attributes:
    width (int): width of the rectangle
    height (int): height of the rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define the class of the Square.

    Args:
        Rectangle (Rectangle): rectangle
    """

    def __init__(self, size):
        """Creates new instances of class Square.

        Args:
            size (int): size of 1 side of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string representative of the square.

        Returns:
            str: square.
        """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

    def area(self):
        """Calculate the area of a square.

    Returns:
        int: the area of the square.
        """
        return self.__size ** 2
