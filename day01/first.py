#!/usr/bin/env python3
import re

def challenge(filename: str) -> int:
	result = 0
	with open(filename, 'r') as fichier:
		for line in fichier.readlines():
			digits = re.findall('[0-9]', line)
			result += int(f"{digits[0]}{digits[-1]}")
	return result

print("sample: ", challenge("sample1"))
print("input: ", challenge("input"))

