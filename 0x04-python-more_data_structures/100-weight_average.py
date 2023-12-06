#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = sum([b * c for b, c in my_list])
    ans = a / sum([c for b, c in my_list])
    return ans
