#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 10:
    digit = digit * -1
if digit > 5:
    print(f"Last digit of {number:d} is {digit:d} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number:d} is {digit:d} and is 0")
else:
    str ="Last digit of {} is {} and is less than 6 and not 0"
    print(str.f(number, digit))
