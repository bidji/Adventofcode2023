#!/usr/bin/env python3


def hash_ascii(sequence: str) -> int:
    value = 0
    for c in sequence:
        value += ord(c)
        value *= 17
        value = value % 256
    return value


def challenge(filename: str) -> int:
    sequences = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            line = line.replace('\n', '')
            sequences.extend(line.split(','))

    result = 0
    for sequence in sequences:
        result += hash_ascii(sequence)

    return result


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
