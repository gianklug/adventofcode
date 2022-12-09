#!/usr/bin/python3
import sys

sys.setrecursionlimit(10000)
line = open("6/input.txt", "r").readlines()[0].strip()


# This was the original solution I came up with, using a recursive approach
def get_unique_sequence_recursive(idx, length, minlen):
    if int(length) >= minlen-1:
        return idx-minlen, length, minlen
    
    if (len(set(str(line[idx-minlen:idx])))) == minlen:
        length += 1
    else:
        length = 0

    return get_unique_sequence_recursive(idx+1, length, minlen)
    
# As I reached the recursion limit for the second part I decided to just throw ChatGPT
# (https://chat.openai.com) at the problem and it solved the problem in a much nicer
# way than I imagnied of doing it.
def get_unique_sequence_iterative(marker_length):
    # Initialize the current marker variable and the result variable
    current_marker = ""
    result = None
    
    # Loop through the characters in the input string
    for c in line:
        # Add the current character to the current marker
        current_marker += c
        # If the current marker has the required length, check if it is a marker
        if len(current_marker) == marker_length:
            if len(set(current_marker)) == marker_length:
                # If the current marker is a valid marker, set the result and break the loop
                result = line.index(current_marker) + marker_length
                break
            else:
                # If the current marker is not a valid marker, remove the first character from it
                current_marker = current_marker[1:]
    # Return the result
    return result


print(get_unique_sequence_recursive(1, 0, 4)[0])
print(get_unique_sequence_iterative(14))
#print(len(line))