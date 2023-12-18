#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    last = 0
    try:
        for a in range(x):
            print(my_list[a], end="")
            last += 1
    except:
        print()
        return(last)
    print()
    return(last)
