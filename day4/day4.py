"""
Advent of code: Day 4
    Part 1: Count valid passports with less conditions
    Part 2: Count valid passports with more conditions
"""

import re

conditions = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part_two(item_key, item_value):
    """
    Check conditions with every fields of passports
    """

    if item_key == conditions[0]:
        return int(item_value) in (1920, 2002)

    if item_key == conditions[1]:
        return int(item_value) in (2010, 2020)

    if item_key == conditions[2]:
        return int(item_value) in (2020, 2030)

    if item_key == conditions[3]:
        if item_value[-2:] == "cm":
            return int(item_value[:-2]) in (150, 193)
        if item_value[-2:] == "in":
            return int(item_value[:-2]) in (59, 76)
        return int(item_value) in (59, 76)

    if item_key == conditions[4]:
        return bool(re.match(r"^#([a-f]|[0-9]){6}$", item_value))

    if item_key == conditions[5]:
        ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return item_value in ecl

    if item_key == conditions[6]:
        return bool(re.match(r"[0-9]{9}$", item_value))

    return False

# Import data to list
with open("entries.txt") as file:
    data = list(line.rstrip() for line in file)

count_one = 0
count_two = 0
fields_one = 0
fields_two = 0

for line in data[:12]:
    # Count fields when lines is not empty
    if len(line) != 0:
        split_line = re.split(r" ", line)

        for field in split_line:
            key = re.split(r"\:", field)[0]
            value = re.split(r"\:", field)[1]

            print("{}\t{}\t{}".format(key, value, part_two(key, value)))

            fields_one += 1 if key in conditions else 0
            fields_two += 1 if part_two(key, value) else 0
            
            print(fields_two)

        continue

    # Count valid passports from count_fields
    # then reset the count_fields
    count_one += 1 if fields_one == 7 else 0
    count_two += 1 if fields_two == 7 else 0

    fields_one = 0
    fields_two = 0

# Print result
print("Part One: {}".format(count_one))
print("Part Two: {}".format(count_two))
