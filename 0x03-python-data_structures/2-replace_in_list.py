#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    count = 0
    for i in my_list:
        count += 1
    if idx < count:
        my_list[idx] = element
        return my_list
    else:
        return my_list
