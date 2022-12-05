#!/usr/bin/python3

with open("2/input.txt", "r") as f:
    lines = f.readlines()

def won(p1, p2):
    winning = [
        ["A", "Y"],
        ["B", "Z"],
        ["C", "X"]
    ]
    return [p1, p2] in winning

def get_score(p1, p2):
    
    if p2 == "X":
        fscore = 1
    elif p2 == "Y":
        fscore = 2
    else:
        fscore =3
    
    if p1 == p2.replace("X","A").replace("Y","B").replace("Z","C"):
        score = 3
    elif won(p1, p2):
        score = 6
    else:
        score = 0
    
    print(f"{p1} + {p2} = {fscore} and {score}")
    return score + fscore

total = 0
for line in lines:
    split = line.strip().split(" ")
    total += get_score(split[0], split[1])

print(f"Part one: {total}")
