#!/usr/bin/env python3


def rocks_still_movable_north(platform: [[str]]) -> bool:
    for j in range(1, len(platform)):
        for i in range(len(platform[j])):
            if platform[j][i] == 'O' and platform[j - 1][i] == '.':
                return True
    return False


def move_rocks_north(platform: [[str]]) -> None:
    for j in range(1, len(platform)):
        for i in range(len(platform[j])):
            if platform[j][i] == 'O' and platform[j - 1][i] == '.':
                # switch position
                platform[j - 1][i] = 'O'
                platform[j][i] = '.'


def rocks_still_movable_south(platform: [[str]]) -> bool:
    for j in range(0, len(platform) - 1):
        for i in range(len(platform[j])):
            if platform[j][i] == 'O' and platform[j + 1][i] == '.':
                return True
    return False


def move_rocks_south(platform: [[str]]) -> None:
    for j in range(0, len(platform) - 1):
        for i in range(len(platform[j])):
            if platform[j][i] == 'O' and platform[j + 1][i] == '.':
                # switch position
                platform[j + 1][i] = 'O'
                platform[j][i] = '.'


def rocks_still_movable_west(platform: [[str]]) -> bool:
    for i in range(1, len(platform[0])):
        for j in range(len(platform)):
            if platform[j][i] == 'O' and platform[j][i - 1] == '.':
                return True
    return False


def move_rocks_west(platform: [[str]]) -> None:
    for i in range(1, len(platform[0])):
        for j in range(len(platform)):
            if platform[j][i] == 'O' and platform[j][i - 1] == '.':
                # switch position
                platform[j][i - 1] = 'O'
                platform[j][i] = '.'


def rocks_still_movable_east(platform: [[str]]) -> bool:
    for i in range(0, len(platform[0]) - 1):
        for j in range(len(platform)):
            if platform[j][i] == 'O' and platform[j][i + 1] == '.':
                return True
    return False


def move_rocks_east(platform: [[str]]) -> None:
    for i in range(0, len(platform[0]) - 1):
        for j in range(len(platform)):
            if platform[j][i] == 'O' and platform[j][i + 1] == '.':
                # switch position
                platform[j][i + 1] = 'O'
                platform[j][i] = '.'


def detect_cycle(results: [int]):
    for first in range(len(results)):
        for second in range(first + 1, len(results)):
            if results[first] == results[second]:
                # we may have found a cycle
                inc = 1
                while (second + inc < len(results)
                       and results[first + inc] == results[second + inc]):
                    inc += 1
                    if (inc > 2 and inc % 2 == 0 and results[first:first + int(inc / 2)] ==
                            results[first + int(inc / 2):first + inc]):
                        # cycle found
                        return first, int(inc / 2)
    return -1, 0


def challenge(filename: str) -> int:
    platform = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '')
            platform.append([*line])

    results = []
    for n in range(200):
        # move rocks north until it's not possible anymore
        while rocks_still_movable_north(platform):
            move_rocks_north(platform)

        # move rocks west until it's not possible anymore
        while rocks_still_movable_west(platform):
            move_rocks_west(platform)

        # move rocks south until it's not possible anymore
        while rocks_still_movable_south(platform):
            move_rocks_south(platform)

        # move rocks north until it's not possible anymore
        while rocks_still_movable_east(platform):
            move_rocks_east(platform)

        result = 0
        for j in range(len(platform)):
            result += platform[j].count('O') * (len(platform) - j)
        results.append(result)

    start, length = detect_cycle(results)
    cycle = results[start:start+length]

    # position in cycle for step 1000000000
    position = (1000000000 - start) % length
    return cycle[position - 1]


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))


