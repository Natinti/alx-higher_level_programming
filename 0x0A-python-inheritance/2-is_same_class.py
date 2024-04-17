#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class
; otherwise False.
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance

    Args:
    obj (a_class): object to check type.
    a_class (type): type of type to check.

    Return:
        boolean: True or False
    """
    if type(obj) is not a_class:
        return False
    return isinstance(type(obj), a_class)

