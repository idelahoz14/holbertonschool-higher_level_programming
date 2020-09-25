#!/usr/bin/python3
"""Documentation for simple add integer function"""


def add_integer(a, b=98):
    """Adds two integers together
    Args:
        a (int): first value to add
        b (int, optional): second value to add
    Returns:
        the sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
