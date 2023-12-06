#!/usr/bin/env python3
import re


def challenge(filename: str) -> int:
	result = 0

	with open(filename, 'r') as data:
		for line in data.readlines():
			texts = line.replace('\n', '').split(':')[1].split('|')
			winnings = re.findall('[0-9]+', texts[0])
			numbers = re.findall('[0-9]+', texts[1])
			nb_winnings = len(set(numbers).intersection(winnings))

			if nb_winnings > 0:
				result += 2 ** (nb_winnings - 1)

	return result


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
