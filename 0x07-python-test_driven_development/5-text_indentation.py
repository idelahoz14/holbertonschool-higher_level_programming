#!/usr/bin/python3
"""Text idenattion"""


def text_indentation(text):
    """This function splits a string of text according to punctuation
    Args:
        text (str): the string of text to split
    Raises:
        TypeError: if the text called with the program is not a string
    """
    if (text):
        if type(text) is str:
            comp = ['.', '?', ':']
            new_text = ""
            for elem in text:
                new_text += elem
                if elem in comp:
                    print(new_text.strip())
                    print()
                    new_text = ""
            print(new_text.strip(), end="")
        else:
            raise TypeError("text must be a string")
