#!/usr/bin/python3
"""Function that read txt file"""


def read_file(filename=""):
    """Read a txt file with UTF8 encode"""

    with open(filename,'r') as reader:
        reader_print = reader.read()
        print(reader_print, end="")
