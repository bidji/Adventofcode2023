#!/usr/bin/env python3


class Galaxy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.expansion_shift = 999999

    def __repr__(self):
        return "{" + f"x: {self.x}, y: {self.y}" + "}"

    def distance_from(self, galaxy, universe: [[str]]):
        xmin = min(self.x, galaxy.x)
        xmax = max(self.x, galaxy.x)
        ymin = min(self.y, galaxy.y)
        ymax = max(self.y, galaxy.y)
        # starting with normal x distance
        distance = xmax - xmin
        # then adding expansion found
        for c in universe[ymin][xmin:xmax]:
            if c == '*':
                distance += self.expansion_shift
        # adding normal y distance
        distance += self.y - galaxy.y if self.y > galaxy.y else galaxy.y - self.y
        # then adding expansion found
        for line in universe[ymin:ymax]:
            if line[xmax] == '*':
                distance += self.expansion_shift
        return distance


def challenge(filename: str) -> int:
    universe = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '')
            # deal with line expansion during reading
            if '#' not in [*line]:
                # we will use * to represent expansion
                line = line.replace('.', '*')
            universe.append([*line])

    # deal with column expansion now
    columns = []
    # initialization of columns with first line of universe
    for column in universe[0]:
        columns.append(1 if column == '#' else 0)
    # and then add galaxy found in each column
    for line in universe[1:]:
        for i in range(len(line)):
            columns[i] += 1 if line[i] == '#' else 0
    for x in range(len(columns)):
        if columns[x] == 0:
            for y in range(len(universe)):
                universe[y][x] = '*'

    # store position of each galaxy
    galaxies = []
    for y in range(len(universe)):
        for x in range(len(universe[y])):
            if universe[y][x] == '#':
                galaxies.append(Galaxy(x, y))

    # compute distances
    distances = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            distances += galaxies[i].distance_from(galaxies[j], universe)
    return distances


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
