"""
Advent of code: Day 7
    Part one: Count the number of bags that contain "shiny gold" color
    Part two: Count all the bags with rule
"""

with open("entries.txt", "r") as file:
    data = [line.rstrip() for line in file]

# Part One
# Recursive function to count the color bag
def get_num_bag(color):
    all_colors = []

    # Cut out line which contain color needed to find
    lines = [line for line in data if color in line and line.index(color) != 0]

    # Find the color that contains the original color
    colors = [line[:line.index(" bags")] for line in lines]
    colors = [color for color in colors if color not in all_colors]

    # Append unique colors the the list and find the upper color
    for color in colors:
        all_colors.append(color)
        bags = get_num_bag(color)

        all_colors += bags

    unique_colors = []

    for color in all_colors:
        if color not in unique_colors:
            unique_colors.append(color)
    
    return unique_colors

# Part Two
def get_bag_count(color):
    rule = ""
    
    for line in data:
        if line[:line.index(" bags")] == color:
            rule =  line

    if "no" in rule:
        return 1
    
    rule = rule[rule.index("contain")+8:].split()

    total = 0
    i = 0

    while i < len(rule):
        count = int(rule[i])
        color = rule[i+1] + " " + rule[i+2]
        total += count * get_bag_count(color)
        i += 4
    
    return total + 1