#!/usr/bin/env python3
import re


def challenge(filename: str) -> int:
    result = 0
    with open(filename, 'r') as data:
        for line in data.readlines():
            steps = []

            # build first step with numbers in line
            numbers = []
            for num in re.findall('[0-9-]+', line):
                numbers.append(int(num))
            steps.append(numbers)

            # build needed steps until obtaining only 0
            while not all(num == 0 for (num) in steps[-1]):
                new_step = []
                for i in range(len(steps[-1]) - 1):
                    new_step.append(steps[-1][i + 1] - steps[-1][i])
                steps.append(new_step)

            # build previous value for each step
            steps[-1].insert(0, 0)
            for s in range(len(steps) - 1, 0, -1):
                steps[s - 1].insert(0, steps[s - 1][0] - steps[s][0])

            result += steps[0][0]

    return result


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
