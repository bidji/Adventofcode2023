#!/usr/bin/env python3


def sums(filename: str) -> int:
	result = 0
	with open(filename, 'r') as data:
		for line in data.readlines():
			min_red = 1
			min_green = 1
			min_blue = 1
			for draw in line.split(':')[1].replace('\n', '').split(';'):
				for dices in draw.split(','):
					if 'red' in dices:
						nb_red = int(dices.replace('red', '').replace(' ', ''))
						if nb_red > min_red:
							min_red = nb_red
					if 'green' in dices:
						nb_green = int(dices.replace('green', '').replace(' ', ''))
						if nb_green > min_green:
							min_green = nb_green
					if 'blue' in dices:
						nb_blue = int(dices.replace('blue', '').replace(' ', ''))
						if nb_blue > min_blue:
							min_blue = nb_blue

			result += min_red * min_green * min_blue

	return result


print("example: ", sums(filename="sample"))
print("input: ", sums(filename="input"))
