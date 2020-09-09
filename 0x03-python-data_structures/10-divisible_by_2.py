#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    condition = []
    for i in new_list:
        log = True if i % 2 == 0 else False
        condition.append(log)
    return condition
