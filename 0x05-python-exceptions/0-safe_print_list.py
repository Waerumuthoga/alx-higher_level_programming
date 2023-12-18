#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        last = 0
        for a in range(x):
            print(my_list[a], end="")
            last += 1
    except IndexError:
        print()
        return(last)
    print()
    return(last)
