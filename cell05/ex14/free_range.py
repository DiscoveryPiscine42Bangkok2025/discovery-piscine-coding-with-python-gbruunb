#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    print([i for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1)])