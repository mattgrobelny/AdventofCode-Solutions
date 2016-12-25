#!/usr/bin/env python
#
# Advent of Code: Day 2
# Matt Grobelny

import sys
import numpy

inputfile = "./day2_input.txt"
fh = open(inputfile, 'r')


w, h = 5, 5
bucket = [[int(0)] * w for i in range(h)]

# fill number pad
for i in range(3):
    bucket[1][i+1] = i + 1
    bucket[2][i+1] = i + 4
    bucket[3][i+1] = i + 7

# stat loc
cur_x = 2
cur_y = 2
passcode = ""

last_loc = 0
# last_val = 0
# print bucket
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
            # passcode = passcode + str(bucket[cur_y][cur_x])
            # print dir_letter, last_val, bucket[cur_y][cur_x], passcode

        else:
            continue
            # print dir_letter, last_val, bucket[cur_y][cur_x], passcode
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
