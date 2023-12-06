#!/usr/bin/python3
def best_score(a_dictionary):
    n = 0
    ans = ""
    if a_dictionary:
        for v, h in a_dictionary.items():
            if h > n:
                ans = v
                n = h
        return ans
    else:
        return None
