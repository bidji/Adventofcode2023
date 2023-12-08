#!/usr/bin/env python3


def challenge(filename: str) -> int:
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

    step = 0
    location = 'AAA'
    while location != 'ZZZ':
        location = coords[location][instructions[step % len(instructions)]]
        step += 1

    return step


print("sample1: ", challenge(filename="sample1"))
print("sample2: ", challenge(filename="sample2"))
print("input: ", challenge(filename="input"))
