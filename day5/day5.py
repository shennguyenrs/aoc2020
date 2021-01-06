"""
Advent of code: Day 5
    Part 1: Find the highest seat ID
    Part 2: Find the missing seat ID which continuous range of IDs
"""

from math import floor, ceil

# Import data to list
with open("entries.txt") as file:
    data = list(line.rstrip() for line in file)

seat_id = []

for line in data[:3]:
    top = 127
    bot = 0
    rgt = 0
    lft = 0
    col = 0
    row = 0

    for char in line:
        if char == "F":
            row = floor((top+bot)/2)
            top = row
        elif char == "B":
            row = ceil((top+bot)/2)
            bot = row
        elif char == "L":
            col = floor((rgt+lft)/2)
            rgt = col
        else:
            col = ceil((top+bot)/2)
            lft = col

    print(row*8+col)
    seat_id.append(row*8+col)

# seat_id.sort()
# print(seat_id[len(seat_id)-1])
