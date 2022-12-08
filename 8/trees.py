#!/usr/bin/python3
# I hate my life for this code
lines = [l.strip() for l in open("input.txt", "r").readlines()]

trees = []

rows = len(lines)
cols = len(lines[0])
total = 0
max_score = -1

for r in range(rows):
    for c in range(cols):

        value = lines[r][c]
        visible = False

        if (r == 0) or (c == 0) or (r == len(lines)-1) or (c == len(lines[0])-1):
            visible = True

        left_count = 0
        left_visible = True
        for i in range(c-1, -1, -1):
            left_count += 1
            if lines[r][i] >= value:
                left_visible = False
                break

        right_count = 0
        right_visible = True
        for i in range(c+1, cols):
            right_count += 1
            if lines[r][i] >= value:
                right_visible = False
                break

        top_count = 0
        top_visible = True
        for i in range(r-1, -1, -1):
            top_count += 1
            if lines[i][c] >= value:
                top_visible = False
                break

        bottom_count = 0
        bottom_visible = True
        for i in range(r+1, rows):
            bottom_count += 1
            if lines[i][c] >= value:
                bottom_visible = False
                break

        if left_visible or right_visible or top_visible or bottom_visible:
            total += 1

        score = left_count * right_count * top_count * bottom_count
        if score > max_score:
            max_score = score

print(total)
print(max_score)
