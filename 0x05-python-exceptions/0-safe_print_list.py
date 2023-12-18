#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for a in range(x):
            print(my_list[a], end="")
            a = a + 1
        print()
        return a
    except:
        print()
        return a
    print("\n")
