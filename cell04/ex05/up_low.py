#!/usr/bin/env python3 

txt = input()
for letter in txt:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")