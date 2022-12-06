#!/usr/bin/python3
import string 
import re

with open("5/input.txt", "r") as f:
    lines = f.read()

def parse_boxes(array):
    array = array[::-1]
    rows = len(array)
    columns = len(array[0]) // 4 + 1
    result = [[] for x in range(0, columns)]
    for row in range(1, rows):
        for x in range(0, columns+1):
            char = array[row][x*4-3]
            if char in string.ascii_uppercase:
                result[x-1].append(char)
    return result

def split_lines(txt):
    a, b = txt.split("\n\n")
    return a.split("\n"), b.split("\n")[:-1]

def execute_instruction(txt, boxes, p2=False):
    result = re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", txt)
    target = int(result.group(1))
    source = int(result.group(2))
    destination = int(result.group(3))
    popped_elements = boxes[source-1][-target:]
    boxes[source-1] = boxes[source-1][:-target]
    if not p2:
        popped_elements= popped_elements[::-1]
    boxes[destination-1] += popped_elements
    return boxes

def print_result(p2=False):
    figure, instructions = split_lines(lines)
    boxes = parse_boxes(figure)
    for line in instructions:
        boxes = execute_instruction(line, boxes, p2)
    print(f"Part {'two' if p2 else 'one'}")
    print("".join([ box[-1] for box in boxes ]))

print_result() # Part 1
print_result(p2=True) # Part 2

