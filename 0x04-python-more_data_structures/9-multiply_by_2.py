#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for j in new.keys():
        new[j] = new[j] * 2
        return new
