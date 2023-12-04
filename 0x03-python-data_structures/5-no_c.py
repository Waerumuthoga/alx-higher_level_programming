#!/usr/bin/python3
def no_c(my_string):
    a = my_string.split("c")
    a = "".join(a)
    a = a.split("C")
    a = "".join(a)
    return a
