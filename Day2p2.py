#!/usr/bin/env python
#
# Advent of Code: Day 2 part 2
# Matt Grobelny

import sys
import numpy

inputfile = "./day2_input.txt"
fh = open(inputfile, 'r')


w, h = 7, 7
bucket = [[int(0)] * w for i in range(h)]

# fill for part 2
bucket[1][3] = 1
for i in range(2, 5):
    bucket[2][i] = i
for i in range(1, 6):
    bucket[3][i] = i + 4
bucket[4][2] = "A"
bucket[4][3] = "B"
bucket[4][4] = "C"
bucket[5][3] = "D"

# start locations
cur_x = 2
cur_y = 2
passcode = ""
last_loc = 0

def passout(input_text):
    for i in range(len(input_text)):
        global cur_x
        global cur_y
        global passcode
        dir_letter = input_text[i]
        current_val = 0
        last_val = bucket[cur_y][cur_x]
        cur_x_it = cur_x
        cur_y_it = cur_y
        if dir_letter == 'U':
            cur_y -= 1
        elif dir_letter == 'D':
            cur_y += 1
        elif dir_letter == 'L':
            cur_x -= 1
        elif dir_letter == 'R':
            cur_x += 1

        if bucket[cur_y][cur_x] == 0:
            cur_x = cur_x_it
            cur_y = cur_y_it
        else:
            continue
    # Output last key number
    passcode = passcode + str(bucket[cur_y][cur_x])
    return passcode
    return cur_x
    return cur_y

input_text1 = ""
for line in fh:
    passout(line)
print "passcode"
print passcode
