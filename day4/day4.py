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

    # byr
    if item_key == conditions[0]:
        result = int(item_value) in range(1920, 2002+1)

    # iyr
    elif item_key == conditions[1]:
        result = int(item_value) in range(2010, 2020+1)

    # eyr
    elif item_key == conditions[2]:
        result = int(item_value) in range(2020, 2030+1)

    # hgt
    elif item_key == conditions[3]:
        if item_value[-2:] == "cm":
            result = int(item_value[:-2]) in range(150, 193+1)
        elif item_value[-2:] == "in":
            result = int(item_value[:-2]) in range(59, 76+1)
        else:
            result = int(item_value) in range(59, 76+1)

    # hcl
    elif item_key == conditions[4]:
        result = bool(re.match(r"^#([a-f]|[0-9]){6}$", item_value))

    # ecl
    elif item_key == conditions[5]:
        ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        result = item_value in ecl

    # pid
    elif item_key == conditions[6]:
        result = bool(re.match(r"[0-9]{9}$", item_value))

    else:
        result = False

    return result

# Import data to list
with open("entries.txt") as file:
    data = list(line.rstrip() for line in file)

count_one = 0
count_two = 0
fields_one = 0
fields_two = 0

length = len(data)

for line in data:
    length -= 1

    # Count fields when lines is not empty
    if len(line) != 0:
        split_line = re.split(r" ", line)

        for field in split_line:
            key = re.split(r"\:", field)[0]
            value = re.split(r"\:", field)[1]

            fields_one += 1 if key in conditions else 0
            fields_two += 1 if part_two(key, value) else 0

        if length != 0:
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
