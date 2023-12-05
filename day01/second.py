#!/usr/bin/env python3
import re
import sys

def sum(filename: str) -> int:
	result = 0
	numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

	with open(filename, 'r') as fichier:
		for line in fichier.readlines():
			text = line.replace('zerone', 'zeroone').replace('oneight','oneeight').replace('twone', 'twoone')
			text = text.replace('threeight', 'threeeigt').replace('fiveight', 'fiveeight').replace('sevenine', 'sevennine')
			text = text.replace('eightwo', 'eighttwo').replace('eighthree', 'eightthree').replace('nineight', 'nineeight')
			digits = re.findall(f"[0-9]|{'|'.join(numbers.keys())}", text)
			try:
				first = int(digits[0])
			except ValueError:
				first = int(numbers[digits[0]])
			try:
				last = int(digits[-1])
			except ValueError:
				last = int(numbers[digits[-1]])
			result += int(f"{first}{last}")

	return result

print('sample:', sum("sample2"))
print('input:', sum("input"))

