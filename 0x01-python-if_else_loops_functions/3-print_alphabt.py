#!/usr/bin/python3
print("{}".format(''.join(chr(a) for a in range(97, 123) if chr(a) not
    in ['q', 'e'])), end='')
