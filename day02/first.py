#!/usr/bin/env python3


def sums(filename: str, nb_red: int, nb_green: int, nb_blue: int) -> int:
	result = 0
	with open(filename, 'r') as data:
		for line in data.readlines():
			game_id = int(line.split(':')[0].replace('Game ', ''))
			game_ok = True
			for draw in line.split(':')[1].replace('\n', '').split(';'):
				for dices in draw.split(','):
					if 'red' in dices:
						if int(dices.replace('red', '').replace(' ', '')) > nb_red:
							game_ok = False
					if 'green' in dices:
						if int(dices.replace('green', '').replace(' ', '')) > nb_green:
							game_ok = False
					if 'blue' in dices:
						if int(dices.replace('blue', '').replace(' ', '')) > nb_blue:
							game_ok = False

			if game_ok:
				result += game_id

	return result


print("sample: ", sums(filename="sample", nb_red=12, nb_green=13, nb_blue=14))
print("input: ", sums(filename="input", nb_red=12, nb_green=13, nb_blue=14))
