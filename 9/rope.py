#!/usr/bin/python3
import numpy

# Read the input
lines = [l.strip() for l in open("9/input.txt", "r").readlines()]

# Move a tail element based on its head element
def move_tail(head, tail):
    difference = tuple(numpy.subtract(head,tail))
    # 1 dot distance is fine
    if abs(difference[0]) <=1 and abs(difference[1]) <=1:
        return tail # do nothing
    # Do we have to move diagonally?
    if ((abs(difference[0]) >= 2 and abs(difference[1]) >= 1) or (abs(difference[0]) >= 1 and abs(difference[1]) >= 2)):
        x, y = -1 if difference[0] < 0 else 1, -1 if difference[1] < 0 else 1 # Take +- into account
        tail = tuple(numpy.add(tail, (x, y))) # Add the new values to the tuple
    else:
        if (abs(difference[0]) == 2): # Move into the x direction
            x, y = -1 if difference[0] < 0 else 1, 0 # Take +- into acount
        elif (abs(difference[1]) == 2): # Move into the y direction
            x, y = 0,  -1 if difference[1] < 0 else 1 # Take +- into acount
        tail = tuple(numpy.add(tail, (x, y))) # Add the new values to the tuple
    return tail # Return again

# Wrapper function for different counts
def calculate_dots(count):
    # Prepare the rope
    rope = [(0,0) for _ in range(0,count)]
    # Use a set as coordinates are unique
    coordinates = set()
    for l in lines: # for every line
        action, amount = l.split(" ") # We can nicely split by space
        for _ in range(int(amount)):
            # We can simplify the operations by mapping the letters to vectors
            rope[0] = tuple(numpy.add(rope[0], {"L": (-1, 0), "R": (1,0), "U": (0,1), "D": (0,-1)}[action]))
            for x in range(1, count): # Move every rope piece
                rope[x] = move_tail(rope[x-1],rope[x]) 
            # Add the last rope piece to the array
            coordinates.add(rope[-1])
    return(len(coordinates))
# Solve it!
print(f"Part 1: {calculate_dots(2)}")
print(f"Part 2: {calculate_dots(10)}")