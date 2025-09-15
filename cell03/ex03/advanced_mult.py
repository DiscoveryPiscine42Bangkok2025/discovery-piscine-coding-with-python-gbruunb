#!/usr/bin/env python3 

import sys

if len(sys.argv) > 1:
    param = sys.argv[1]
    print("none")
else:
    table = 0
    max_table = 10
    max_idx = 10
    while table <= max_table:
        idx = 0
        print(f"Table de {table}:", end=" ")
        while idx <= max_idx:
            print(table * idx, end=" ")
            idx += 1
        print()
        table += 1
