#!/usr/bin/python3

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

a = 18
print(factorial(a))