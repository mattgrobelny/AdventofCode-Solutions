#!/usr/bin/env python
#
# Advent of Code: Day 1
# Matt Grobelny
# http://adventofcode.com/2016/day/1
#

import math
adventofcode_day1 = 'L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2'

adventofcode_day1 = adventofcode_day1.replace(" ", "")
adventofcode_day1 = adventofcode_day1.split(',')

# start cordinates
start = [0, 0]

# start orientation (North)
cur_ori = 0
dir_addition = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for direction in adventofcode_day1:
    # pull of data from string
    turn = str(direction[0])  # orietation
    walk_val = int(direction[1:])  # walking distance
    if turn == "R":
        cur_ori += 1
        add_dir = dir_addition[cur_ori % 4]  # find orientation rap around in list with %
        # update walking cordinates based on direction and distance
        start = [start[0] + add_dir[0] * walk_val, start[1] + add_dir[1] * walk_val]
    else:
        # repeat for "L"
        cur_ori -= 1
        add_dir = dir_addition[cur_ori % 4]
        start = [start[0] + add_dir[0] * walk_val, start[1] + add_dir[1] * walk_val]
    end = start

# shortest path (number of blocks)
distance = end[0] + end[1]
print distance
