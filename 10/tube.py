#!/usr/bin/python3

instructions = [x.strip() for x in open("10/input.txt", "r").readlines()]

def get_values_after_n_cycles(cycles, instructions):
    start_value = 1
    buffer = 0
    index = 0
    for i in range(0, cycles):
        current = instructions[index]
        if "noop" in current:
            index += 1
        elif buffer != 0:
            start_value += buffer
            buffer = 0
            index += 1
        else:
            buffer = int(instructions[index].split("addx ")[1])
    return start_value

cycles_wanted = [20, 60, 100, 140, 180, 220]
# Print the Solution for part 1
print(f"Part 1: {sum([c*get_values_after_n_cycles(c, instructions) for c in cycles_wanted])}")

display = ""
for i in range(6):
    for j in range(0, 40):
        # Get the cycles for the current position
        v = get_values_after_n_cycles(j+40*i, instructions)
        if j == v or j == v-1 or j == v+1:
            display += "#"
        else:
            display += " " # . would make it too unreadable imo
    display += "\n" # Next line
print("Part 2:")
print(display)
