#!/usr/bin/python3

# Read in the text
with open("1/input.txt", "r") as file:
    text = file.read()


# Function for summing an array (could be done way easier wtf)
def sum_array(arr):
    sum = 0
    for el in arr:
        # Prevent empty lines
        if el.replace("\n","") == "":
            continue
        # Add to total
        sum += int(float(el))
    return sum

# Split into elves
elves = text.split("\n\n")

# Sum the calories
calories_total = [sum_array(el.replace("\n","")) for el in elves ]

# Result for part one
print(f"Top elve: {max(calories_total)}")

# Result for part two
sorted_cals = sorted(calories_total, reverse=True)
result = sorted_cals[0] + sorted_cals[1] + sorted_cals[2]
print(f"Top three elves: {result}")
