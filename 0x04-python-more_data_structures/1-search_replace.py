#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for m in my_list:
        if m == search:
            new.append(replace)
        else:
            new.append(m)
    return new
