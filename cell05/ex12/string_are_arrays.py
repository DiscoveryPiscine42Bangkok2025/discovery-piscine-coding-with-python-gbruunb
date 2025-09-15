#!/usr/bin/env python3

import sys

if len(sys.argv) != 2 or sys.argv[1].count("z") == 0:
    print("none")
else:
    for i in range(sys.argv[1].count("z")):
        print("z", end="")
    print()