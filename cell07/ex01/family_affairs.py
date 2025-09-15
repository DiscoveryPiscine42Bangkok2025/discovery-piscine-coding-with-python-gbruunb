#!/usr/bin/env python3

def find_the_redheads(dupont_family):
    dupont_family_filter = {key: value for key, value in dupont_family.items() if value == 'red'}
    firstname_list = list(dupont_family_filter.keys())
    return firstname_list

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(dupont_family))