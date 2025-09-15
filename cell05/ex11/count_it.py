#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    del sys.argv[0]
    print("parameters:", len(sys.argv))
    for i in sys.argv:
        print(f"{i}: {len(i)}")
