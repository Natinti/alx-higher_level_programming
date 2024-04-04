#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list that are integers
    in the program

    Args:
        my_list (list): The list is to print elements from.
        x (int): This is the number of elements of my_list to print

    Return:
        The number of elements that will be printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
