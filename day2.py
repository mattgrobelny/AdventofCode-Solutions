#!/usr/bin/env python
#
# Advent of Code: Day 2
# Matt Grobelny

import sys
import numpy

inputfile = "./day2_input.txt"
fh = open(inputfile, 'r')

input_text1 = ""
for line in fh:
    input_text1 = input_text1 + line

w, h = 5, 5
bucket = [[None] * w for i in range(h)]

# fill number pad
for i in range(3):
    bucket[1][i+1] = i + 1
    bucket[2][i+1] = i + 4
    bucket[3][i+1] = i + 7

# stat loc
cur_loc = [2, 2]
passcode = ""

# print bucket
for i in range(len(input_text1)):
    dir_letter = input_text1[i]
    last_loc = []
    current_val = ""

    last_loc = cur_loc
    print current_val
    try:
        current_val = bucket[cur_loc[0]][cur_loc[1]]
    except IndexError:
        current_val = 'None'
    if current_val == 'None':
        print "in this loop"
        cur_loc = last_loc
        passcode = passcode + str(bucket[cur_loc[0]][cur_loc[1]])
    else:
        if dir_letter == 'U':
            last_loc = cur_loc
            cur_loc[0] -= 1
        elif dir_letter == 'D':
            last_loc = cur_loc
            cur_loc[0] += 1
        elif dir_letter == 'L':
            last_loc = cur_loc
            cur_loc[1] -= 1
        else:
            # dir_letter == "R":
            last_loc = cur_loc
            cur_loc[1] += 1

print passcode
