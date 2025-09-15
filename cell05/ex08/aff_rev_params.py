#!/usr/bin/env python3

import sys

if len(sys.argv) <= 2:
    print("none")
else:
    del sys.argv[0]
    sys.argv.reverse()
    for i in sys.argv:
        print(i)