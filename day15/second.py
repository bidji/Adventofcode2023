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

    # init list with 256 boxes
    hashmap = []
    for n in range(256):
        hashmap.append({})
    for sequence in sequences:
        if '=' in sequence:
            # we need to add this sequence in the right box
            label = sequence.split('=')[0]
            focal = int(sequence.split('=')[1])
            num_box = hash_ascii(label)
            hashmap[num_box][label] = focal
        if '-' in sequence:
            label = sequence.split('-')[0]
            # we need to remove this label
            num_box = hash_ascii(label)
            if label in hashmap[num_box]:
                del hashmap[num_box][label]

    result = 0
    for n in range(256):
        num_slot = 1
        for focal in hashmap[n]:
            result += (n + 1) * num_slot * hashmap[n][focal]
            num_slot += 1

    return result


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
