#!/usr/bin/env python
#
# Advent of Code: Day 3 part 1
# Matt Grobelny

import sys
import numpy

inputfile = "./day3_input.txt"
fh = open(inputfile, 'r')

def twosides_greater(list):
    list.sort()
    # test for possible triangle
    if int(list[0]) + int(list[1]) > int(list[2]) and (int(list[2]) + int(list[1])) > int(list[0]) and (int(list[0]) + int(list[2])) > int(list[1]):
        global pos_tri
        pos_tri += 1
pos_tri = 0

for line in fh:
    line = line.strip('\n')
    line = line.split(' ')
    val_list = []
    for val in line:
        if val.isdigit():
            val_list.append(val)
        else:
            continue
    twosides_greater(val_list)
print pos_tri
