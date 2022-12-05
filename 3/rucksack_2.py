#!/usr/bin/python3
import string

with open("3/input.txt", "r") as f:
    lines = f.readlines()

def split_into_groups(arr):
    # yes, this is ugly
    output = [[] for i in range(len(arr)//3)] 
    for index, line in enumerate(arr):
        index = index // 3
        print(index)
        output[index].append(line.strip())
    return output

def is_in_all_three(item):
    for a in list(item[0]):
        if a in list(item[1]):
            if a in list(item[2]):
                return a


def get_priority(letter):
    alph = list(string.ascii_lowercase + string.ascii_uppercase)
    return alph.index(letter)+1

total = 0
for index, group in enumerate(split_into_groups(lines)):
    matching = is_in_all_three(group)
    priority = get_priority(matching)
    total += priority
    print(f"Group no. {index}: Matching '{matching}', Prio {priority}")

print(total)