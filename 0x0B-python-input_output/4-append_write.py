#!/usr/bin/python3
"""appends a text in file"""


def append_write(filename="", text=""):
    """appends text"""

    with open(filename, 'a', encoding = 'utf-8') as reader:
        reader.write(text)
        return len(text)
