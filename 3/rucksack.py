#!/usr/bin/python3
import string

with open("3/input.txt", "r") as f:
    lines = f.readlines()


def split_array(arr):
    a = arr[:len(arr)//2]
    b = arr[len(arr)//2:]
    return [a, b]

def get_priority(letter):
    alph = list(string.ascii_lowercase + string.ascii_uppercase)
    return alph.index(letter)+1

def is_duplicate(l1, l2):
    for item in l1:
        if item in l2:
            return get_priority(item)
    return 0


prio = 0
for line in lines:
    line = line.strip()
    items = list(line)
    split = split_array(items)
    prio += is_duplicate(split[0], split[1])

print(prio)