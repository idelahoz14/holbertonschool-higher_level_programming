#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    i_set = set(set_1)
    v_set = set(set_2)
    return (i_set ^ v_set)
