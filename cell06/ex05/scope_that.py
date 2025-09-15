#!/usr/bin/env python3

def add_one(a):
    a += 1
    return a

num = 10
print("Before calling add_one:", num)
num = add_one(num)
print("After calling add_one:", num)
