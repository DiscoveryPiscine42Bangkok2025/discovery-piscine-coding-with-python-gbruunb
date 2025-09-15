#!/usr/bin/env python3 

age = int(input("Please tell me your age: "))
print("You are currently 15 years old.")
year = 10
while year <= 30:
    print(f"In {year} years, you'll be {age + year} years old.")
    year += 10