#!/usr/bin/env python3

import sys

def shrink(word):
    print(word[0:8])
def enlarge(word):
    print(word, end="")
    print("Z" * (8 - len(word)))

if len(sys.argv) < 2:
    print("none")
else:
    del sys.argv[0]
    for i in sys.argv:
        if len(i) < 8:
            enlarge(i)
        elif len(i) > 8:
            shrink(i)
        else:
            print(i)