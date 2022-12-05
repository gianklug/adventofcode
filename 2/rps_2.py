#!/usr/bin/python3

with open("2/input.txt", "r") as f:
    lines = f.readlines()

def get_action(p1, p2):
    actions = {
        "Z": {
            "A": 2,
            "B": 3,
            "C": 1
        },
        "Y": {
            "A": 1,
            "B": 2,
            "C": 3
        },
        "X": {
            "A": 3,
            "B": 1,
            "C": 2
        }

    }
    return actions[p2][p1]

def get_score(p1, p2):
    
    if p2 == "X":
        wscore = 0
    elif p2 == "Y":
        wscore = 3
    else:
        wscore = 6
    
    wscore += get_action(p1, p2)
    return wscore

total = 0
for line in lines:
    split = line.strip().split(" ")
    total += get_score(split[0], split[1])

print(f"Part two: {total}")
