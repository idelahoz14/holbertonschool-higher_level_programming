#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return None
        