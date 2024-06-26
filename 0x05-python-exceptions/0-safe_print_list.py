#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print the x elements of a list.

    Args: my_list(list): This is the list to print
    elements from x (int): The number of elements of my_list to print.

    Return:
    The number of elements that will be printed in the program.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
