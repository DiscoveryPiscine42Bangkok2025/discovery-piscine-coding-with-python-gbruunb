#!/usr/bin/env python3

def array_of_names(person):
    name_list = []
    for key, value in person.items():
        name = key.capitalize() + " " + value.capitalize()
        name_list.append(name)
    
    return name_list
        

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))