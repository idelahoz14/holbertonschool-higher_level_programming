#!/usr/bin/python3
"""Function that write a sting to a txt file"""


def write_file(filename="", text=""):
    """Write a string to a txt file"""

    with open(filename, 'w', encoding='utf-8') as reader:
        reader.write(text)
        return len(text)
