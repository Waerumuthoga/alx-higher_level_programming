#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for w in my_list:
        if w % 2 is 0:
            new.append(True)
        else:
            new.append(False)
    return new
