#!/usr/bin/env python3


def challenge(filename: str) -> int:
    with open(filename, 'r') as data:
        duration = int(data.readline().split(':')[1].replace(' ', ''))
        record = int(data.readline().split(':')[1].replace(' ', ''))

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
