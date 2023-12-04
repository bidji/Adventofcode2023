#!/usr/bin/env python3
import re


def sums(filename: str) -> int:
	result = 0
	matrix = []

	# construction d'une matrice
	line_length = 0
	nb_lines = 0
	with open(filename, 'r') as data:
		for line in data.readlines():
			text = line.replace('\n', '')
			line_length = len(line) - 1
			matrix.append([*text])
			nb_lines += 1

	# recherche des nombres
	with open(filename, 'r') as data:
		line_number = 0
		for line in data.readlines():
			for match in re.finditer('[0-9]+', line):
				number = match.group(0)
				startx = max(0, match.start() - 1)
				endx = min(line_length, match.end() + 1)
				starty = max(0, line_number - 1)
				endy = min(nb_lines, line_number + 1 + 1)

				valid = False
				for y in range(starty, endy):
					for x in range(startx, endx):
						if re.match('[^0-9.]', matrix[y][x]):
							valid = True

				if valid:
					result += int(number)

			line_number += 1

	return result


print("example: ", sums(filename="sample"))
print("input: ", sums(filename="input"))
