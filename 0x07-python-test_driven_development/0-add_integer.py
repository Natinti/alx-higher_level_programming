#!/usr/bin/python3
"""

This is a module created by a function to add two numbers

"""


def add_integer(a, b=98):
    """ this is a function that add two integer and/or float numbers

    Args:
    a: this is the first number
    b: this is the second number

    Returns:
        The results of the addition of two assigned numbers

    Raises:
    TypeError: If a or b are not integer or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an insteger")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
