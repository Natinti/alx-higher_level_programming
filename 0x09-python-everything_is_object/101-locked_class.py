#!/usr/bin/python3
""" LockedClass - This defines a lockedclass
"""


class LockedClass:
    """
    this will prevent dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name.

    Attribute:
        first_name (str): first name of something.
    """

    __slots__ = ['first_name']

    def __init__(self):
        """This creates new instances of Locked Class. """

        self.first_name = "first_name"
