#!/usr/bin/env python3
import re


def sums(filename: str) -> int:
	result = 0
	numbers = []

	# construction d'une matrice
	line_length = 0
	nb_lines = 0
	with open(filename, 'r') as data:
		for line in data.readlines():
			numbers.append(list(re.finditer('[0-9]+', line)))
			line_length = len(line) - 1
			nb_lines += 1

	# recherche des nombres
	with open(filename, 'r') as data:
		line_number = 0
		for line in data.readlines():
			for match in re.finditer('[*]', line):
				startx = max(0, match.start() - 1)
				endx = min(line_length, match.end() + 1)
				starty = max(0, line_number - 1)
				endy = min(nb_lines, line_number + 1 + 1)

				valids = []
				for y in range(starty, endy):
					for number in numbers[y]:
						x = set(range(startx, endx))
						if len(x.intersection(range(number.start(), number.end()))) > 0:
							valids.append(int(number.group(0)))

				if len(valids) > 1:
					value = 1
					for valid in valids:
						value *= valid
					result += value

			line_number += 1

	return result


print("example: ", sums(filename="sample"))
print("input: ", sums(filename="input"))
