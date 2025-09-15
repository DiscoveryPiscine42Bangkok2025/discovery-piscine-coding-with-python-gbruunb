#!/usr/bin/env python3 

num = input("Give me a number: ")
if "." in num:
    num_split = num.split(".")
    if int(num_split[1]) == 0:
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("This number is an integer.")