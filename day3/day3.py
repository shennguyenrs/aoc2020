"""
Advent of code: Day 3
    Part 1: Count tree with slope is right 3 and down 1
    Part 2: Count tree with slope are
        Right   Down
            1      1
            3      1
            5      1
            7      1
            1      2
"""

# Import data to list
with open("entries.txt", "r") as file:
    # Get all lines with blank lines
    lines = (line.rstrip() for line in file)

    # Get lines to list without blank lines
    data = list(line for line in lines if line)

def count_tree(right_slope, down_slope):
    """
    Count tree with right slope and down slope
    Return: counter number of trees
    """

    line_pos = 0
    counter = 0
    x_pos = 0

    while line_pos < len(data):
        counter += 1 if data[line_pos][x_pos]=="#" else 0
        line_pos += down_slope
        x_pos = (x_pos+right_slope)%len(data[0])

    return counter

# Part One
print("Part one: {}".format(count_tree(3, 1)))

# Part Two
slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

result = 1
for slope in slopes:
    result *= count_tree(slope[0], slope[1])

print("Part two: {}".format(result))
