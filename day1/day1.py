"""
Advent of Code 2020 - Day 1

Part 1: Find the couple that have total is 2020
        Then print their multiply result

Part 2: Find the triplet that have its total is 2020
        Then print their multiply result
"""

def find_couple(data_list):
    """
    Find the couple from the data list
    """

    for i in range(len(data_list)-1):
        first = data_list[i]
        second = list(filter(lambda x: x==(2020-first), data_list[i:]))

        if len(second)==1:
            print("The first number is {}".format(first))
            print("The second number is {}".format(second[0]))
            print("Their multiply is {}".format(first * int(second[0])))
            return

def find_triplet(data_list):
    """
    Find the triplet from the data list
    """

    for i in range(len(data_list)-2):
        first = data_list[i]

        for j in range(i+1, len(data_list)):
            second = data_list[j]
            third = list(filter(lambda x: x==(2020-first-second), data_list[j:]))

            if len(third)==1:
                print("The first number is {}".format(first))
                print("The second number is {}".format(second))
                print("The third number is {}".format(third[0]))
                print("Their multiply is {}".format(first * second * int(third[0])))
                return

DataList = list()

# Open file and input data
with open("entries.txt", "r") as file:
    DataList = list(map(int, file.readlines()))

# Sort the list
DataList.sort()

# Find and print out the couple
find_couple(DataList)
print()

# Find and print out the triplet
find_triplet(DataList)
