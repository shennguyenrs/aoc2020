"""
Advent of code: Day 6
    Part 1: Count the distinct answers have "yes" from anyone
    Part 2: Count the distinct answers have "yes" from everyone from groups
"""

with open("entries.txt", "r") as file:
    data = list(line.rstrip() for line in file)

# Part One
line_string = ""
count_ans = 0

for line in data:
    if len(line) != 0:
        line_string += line
    else:
        count_ans += len(set(line_string))
        line_string = ""

print("Part One: {}".format(count_ans))

# Part Two
count_ans = 0
char_dict = dict()
count_line = 0

for line in data:
    if len(line) != 0:
        count_line += 1
        for char in line:
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    else:
        for char, value in char_dict.items():
            if value == count_line:
                count_ans += 1
        count_line = 0
        char_dict.clear()

print("Part Two: {}".format(count_ans))
