"""
Advent of code: Day 2
    Part 1: Count valid passwords which have number of keys in a limit range
    Part 2: Count valid passwords which have keys in specific positions
"""

import re

# Input data to list
with open("entries.txt", "r") as file:
    # Get all lines with blank lines
    lines = (line.rstrip() for line in file)

    # Get lines to list without blank lines
    data = list(line for line in lines if line)

# Count valid passwords
for password in data:
    # Split the string by spaces
    limit = re.split(r"\s+", password)[0]

    lower = int(re.split(r"\-", limit)[0])
    upper = int(re.split(r"\-", limit)[1])

    key = re.split(r"\s+", password)[1][0]

    string = re.split(r"\s+", password)[2]

    part_one +=1 if string.count(key)>=lower and string.count(key)<=upper else 0
    part_two += 1 if key in \
        (string[lower-1], string[upper-1]) and string[upper-1]!=string[lower-1] else 0

print("Part one: {}".format(part_one))
print("Part two: {}".format(part_two))
