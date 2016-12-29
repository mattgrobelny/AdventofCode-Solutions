#!/usr/bin/env python
#
# Advent of Code: Day 3 part 2
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

new_tri_groups_col1 = []
new_tri_groups_col2 = []
new_tri_groups_col3 = []

for line in fh:
    line = line.strip('\n')
    line = line.split(' ')
    val_list = []
    for val in line:
        if val.isdigit():
            val_list.append(val)
        else:
            continue

    new_tri_groups_col1.append(val_list[0])
    new_tri_groups_col2.append(val_list[1])
    new_tri_groups_col3.append(val_list[2])

it_group = [[], [], []]

for i in range(1, len(new_tri_groups_col1) + 1):
    it_group[0].append(new_tri_groups_col1[i - 1])
    it_group[1].append(new_tri_groups_col2[i - 1])
    it_group[2].append(new_tri_groups_col3[i - 1])
    if i % 3 == 0:
        twosides_greater(it_group[0])
        twosides_greater(it_group[1])
        twosides_greater(it_group[2])
        it_group = [[], [], []]
print pos_tri
