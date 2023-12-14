#!/usr/bin/env python3


def rocks_still_movable_north(grid: [[str]]) -> bool:
    for j in range(1, len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 'O' and grid[j - 1][i] == '.':
                return True
    return False


def move_rocks_north(grid: [[str]]) -> None:
    for j in range(1, len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] == 'O' and grid[j - 1][i] == '.':
                # switch position
                grid[j - 1][i] = 'O'
                grid[j][i] = '.'


def challenge(filename: str) -> int:
    grid = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '')
            grid.append([*line])

    # move rocks north until it's not possible anymore
    while rocks_still_movable_north(grid):
        move_rocks_north(grid)

    result = 0
    for j in range(len(grid)):
        result += grid[j].count('O') * (len(grid) - j)

    return result


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
