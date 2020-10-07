#!/usr/bin/python3
"""Function that count n lines"""


def read_lines(filename="", nb_lines=0):
    """Count n lines"""

    with open(filename, 'r') as reader:
        if nb_lines <= 0:
            print(reader.read(), end="")
        else:
            for num_line, line in enumerate(reader):
                if num_line in range(nb_lines):
                    print(line, end="")
