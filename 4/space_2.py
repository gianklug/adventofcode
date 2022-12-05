#!/usr/bin/python3

with open("4/input.txt", "r") as f:
    lines = f.readlines()


def parser(line):
    ranges = line.strip().split(",")
    values_1 = ranges[0].split("-")
    values_2 = ranges[1].split("-")
    range_1 = range(int(values_1[0]), int(values_1[1])+1)
    range_2 = range(int(values_2[0]), int(values_2[1])+1)

    if (set(range_1).intersection(set(range_2))):
        return 1
    return 0


result = sum([parser(x) for x in lines])
print(result)