#!/usr/bin/env python3

num_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = [i + 2 for i in num_arr if i > 5]
new_arr_set = set(new_arr)
print(num_arr)
print(new_arr_set)