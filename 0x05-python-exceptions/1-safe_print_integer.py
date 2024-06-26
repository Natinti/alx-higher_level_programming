#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer that print with "{:d}".format().

    Args:
    value (int): This is the integer to print

    Returns:
    If a TypeError or ValueError occurs - False.
    Otherwise - True.

    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
