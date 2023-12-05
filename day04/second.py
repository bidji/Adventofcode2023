#!/usr/bin/env python3
import re


def sums(filename: str) -> int:
	scratchs = {}
	line_number = 1
	with open(filename, 'r') as data:
		for line in data.readlines():
			# on ajoute la carte courante
			if line_number in scratchs:
				scratchs[line_number] += 1
			else:
				scratchs[line_number] = 1

			texts = line.replace('\n', '').split(':')[1].split('|')
			winnings = re.findall('[0-9]+', texts[0])
			numbers = re.findall('[0-9]+', texts[1])
			nb_winnings = len(set(numbers).intersection(winnings))

			# on ajoute les cartes gagnantes
			for i in range(line_number + 1, line_number + nb_winnings + 1):
				if i in scratchs:
					scratchs[i] += scratchs[line_number]
				else:
					scratchs[i] = scratchs[line_number]

			line_number += 1

	result = 0
	for scratch in scratchs:
		result += scratchs[scratch]
	return result


print("sample: ", sums(filename="sample"))
print("input: ", sums(filename="input"))
