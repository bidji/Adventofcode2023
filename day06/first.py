#!/usr/bin/env python3
import re


def challenge(filename: str) -> int:
    with open(filename, 'r') as data:
        times = re.findall('[0-9]+', data.readline())
        distances = re.findall('[0-9]+', data.readline())

    result = 1
    for i in range(0, len(times)):
        result *= compute(int(times[i]), int(distances[i]))

    return result


def compute(duration, record):
    valids = 0
    for t in range(1, duration - 1):
        if (duration - t) * t > record:
            valids += 1
        else:
            if valids > 0:
                break
    return valids


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
