#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

if lastdigit > 5:
    message = "greater than 5"
elif lastdigit == 0:
    messsage = "0"
else:
    message = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, lastdigit, message))
