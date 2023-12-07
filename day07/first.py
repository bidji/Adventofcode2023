#!/usr/bin/env python3
import re
from functools import cmp_to_key


order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
         '4': 4, '3': 3, '2': 2}


class Hand:
    def __init__(self, hand, hand_type, bid):
        self.hand = hand
        self.hand_type = hand_type
        self.bid = bid

    def __repr__(self):
        return "{" + f"hand: {self.hand}, hand_type: {self.hand_type}, bid: {self.bid}" + "}"

    @staticmethod
    def comparator(a, b):
        if a.hand_type > b.hand_type:
            return -1
        if a.hand_type < b.hand_type:
            return 1
        # same hand_type, we will compare card by card
        for i in range(0, 5):
            if order[a.hand[i]] > order[b.hand[i]]:
                return -1
            if order[a.hand[i]] < order[b.hand[i]]:
                return 1
        return 0


def challenge(filename: str) -> int:
    hands = []
    with open(filename, 'r') as data:
        for line in data.readlines():
            infos = line.replace('\n', '').split(' ')
            hand = infos[0]
            bid = int(infos[1])
            hand_type = get_hand_type(hand)
            hands.append(Hand(hand, hand_type, bid))

    result = 0
    num_hand = 1
    for hand in sorted(hands, key=cmp_to_key(Hand.comparator), reverse=True):
        result += num_hand * hand.bid
        num_hand += 1

    return result


def get_hand_type(hand: str) -> int:
    """
    return type for a hand (6 for Five of a kind, 5 for Four of a kind, 4 for Full house,
    3 for Three of a kind, 2 for Two pair, 1 for One pair, 0 for High card)
    :param hand:
    :return:
    """
    cards = set(order.keys()).intersection([*hand])
    types = []
    for c in cards:
        types.append(len(re.findall(f"{c}", hand)))
    hand_type = 0
    for t in sorted(types, reverse=True):
        if t == 5:
            # Five of a kind
            return 6
        if t == 4:
            # Four of a kind
            return 5
        if t == 3:
            # Three of a kind, we need to check if there is also a pair
            hand_type = 3
        if t == 2:
            # a pair, we check if we already found a Three of a kind
            if hand_type == 3:
                # Full house
                return 4
            # or if we already found a pair
            elif hand_type == 1:
                # Two pair
                return 2
            else:
                hand_type = 1
    return hand_type


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
