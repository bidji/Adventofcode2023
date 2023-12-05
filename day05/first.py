#!/usr/bin/env python3
import re


def sums(filename: str) -> int:
    seeds = []
    maps = {'seed-to-soil': [], 'soil-to-fertilizer': [], 'fertilizer-to-water': [],
            'water-to-light': [], 'light-to-temperature': [], 'temperature-to-humidity': [],
            'humidity-to-location': []}
    key = ''

    max_location = 0
    with open(filename, 'r') as data:
        for line in data.readlines():
            if ' ' not in line:
                continue

            if line.startswith('seeds:'):
                # initial seeds
                for seed in re.findall('[0-9]+', line.split(':')[1]):
                    seeds.append(int(seed))
                continue

            if 'map' in line:
                key = line.split(' ')[0]
                continue

            numbers = re.findall('[0-9]+', line)

            start_dest = int(numbers[0])
            start_source = int(numbers[1])
            size = int(numbers[2])
            maps[key].append({'start': start_source,
                              'end': start_source + size - 1,
                              'shift': start_dest - start_source})
            if key == 'humidity-to-location':
                max_location = max(max_location, start_dest + size)

    # init of lowest with max possible to ensure finding the right min
    lowest_location = max_location
    for seed in seeds:
        location = convert_soil_to_location(seed, maps)
        lowest_location = min(location, lowest_location)

    return lowest_location


def convert_soil_to_location(seed, maps):
    soil = convert(seed, maps['seed-to-soil'])
    fertilizer = convert(soil, maps['soil-to-fertilizer'])
    water = convert(fertilizer, maps['fertilizer-to-water'])
    light = convert(water, maps['water-to-light'])
    temperature = convert(light, maps['light-to-temperature'])
    humidity = convert(temperature, maps['temperature-to-humidity'])
    location = convert(humidity, maps['humidity-to-location'])
    return location


def convert(source, converters):
    converted = source
    for converter in converters:
        if converter['start'] <= source <= converter['end']:
            converted = source + converter['shift']
    return converted


print("sample: ", sums(filename="sample"))
print("input: ", sums(filename="input"))
