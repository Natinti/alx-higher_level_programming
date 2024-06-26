#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a and b."""

    try:
        div = a / b
    except(ZeroDivisionError, FloatingPointError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return(div)
