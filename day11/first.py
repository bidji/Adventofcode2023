#!/usr/bin/env python3


class Galaxy:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{" + f"x: {self.x}, y: {self.y}" + "}"

    def distance_from(self, galaxy):
        distance = self.x - galaxy.x if self.x > galaxy.x else galaxy.x - self.x
        distance += self.y - galaxy.y if self.y > galaxy.y else galaxy.y - self.y
        return distance


def challenge(filename: str) -> int:
    universe = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '')
            # deal with line expansion during reading
            if '#' not in [*line]:
                universe.append([*line])
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
    for y in range(len(universe)):
        for x in range(len(columns) - 1, -1, -1):
            if columns[x] == 0:
                universe[y].insert(x, '.')

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
            distances += galaxies[i].distance_from(galaxies[j])
    return distances


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
