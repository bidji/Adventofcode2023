#!/usr/bin/env python3
from math import lcm


def challenge(filename: str) -> int:
    # build coords from input
    coords = {}
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '').replace(' ', '')
            if len(line) == 0:
                # separator between instructions and coordinates
                continue

            if "=" not in line:
                # instructions
                instructions = [*line]
                continue

            coord_name = line.split('=')[0]
            directions = line.split('=')[1].replace('(', '').replace(')', '').split(',')
            coords[coord_name] = {'L': directions[0], 'R': directions[1]}

    # find starting locations
    start_locations = []
    for coord_name in coords.keys():
        if coord_name.endswith('A'):
            start_locations.append(coord_name)

    # check each starting location alone
    steps = []
    for n in range(0, len(start_locations)):
        steps.append(count_steps(instructions, coords, start_locations[n]))

    return lcm(*steps)


def count_steps(instructions, coords, location):
    # count needed steps to reach destinations
    step = 0
    while not location.endswith('Z'):
        location = coords[location][instructions[step % len(instructions)]]
        step += 1

    return step


print("sample1: ", challenge(filename="sample1"))
print("sample2: ", challenge(filename="sample2"))
print("sample3: ", challenge(filename="sample3"))
print("input: ", challenge(filename="input"))
