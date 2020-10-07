#!/usr/bin/python3
"""Function that count line"""


def number_of_lines(filename=""):
    """Count lines"""

    lines = 0
    with open(filename, 'r') as reader:
        for line in reader:
            lines += 1
    return lines
