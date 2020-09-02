#!/usr/bin/python3
def uppercase(str):
    for container in str:
        i = ord(container)
        if i >= 97 and i <= 122:
            container = chr(i - 32)
        print("{:s}".format(container), end="")
    print("")
