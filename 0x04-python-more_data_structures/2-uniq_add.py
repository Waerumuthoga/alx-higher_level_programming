#!/usr/bin/python3
def uniq_add(my_list=[]):
    ua = 0
    uniq = list(set(my_list))
    for j in uniq:
        ua += j
    return ua
