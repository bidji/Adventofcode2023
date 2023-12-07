#!/usr/bin/env python3
import re
from functools import cmp_to_key


order = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
         '4': 4, '3': 3, '2': 2, 'J': 1}


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

    # extracting jokers
    jokers = 0
    if 'J' in cards:
        jokers = len(re.findall("J", hand))
        cards.remove("J")

    # check specific hands full of jokers
    if jokers == 5:
        # Five of a kind
        return 6

    types = []
    for c in cards:
        nb_cards = len(re.findall(f"{c}", hand))
        types.append(nb_cards)
    hand_type = 0

    for t in sorted(types, reverse=True):
        if t == 5:
            # Five of a kind
            return 6
        if t == 4:
            if jokers == 1:
                # Five of a kind
                return 6
            # Four of a kind
            return 5
        if t == 3:
            if jokers == 2:
                # Five of a kind
                return 6
            if jokers == 1:
                # Four of a kind
                return 5
            # Three of a kind, we need to check if there is also a pair
            hand_type = 3
        if t == 2:
            # it's a pair, further checks needed
            if jokers == 3:
                # Five of a kind
                return 6
            if jokers == 2:
                # Four of a kind
                return 5
            if jokers == 1:
                # it could be a Three of a kind, but only if joker was not used previously
                if hand_type == 3:
                    # joker was used previously on another pair to build a Three of a kind, it's a
                    # Full house
                    return 4
                # joker was not used previously, we can build a Three of a kind
                hand_type = 3
            else:
                # no joker and a pair, we check if we already found a Three of a kind
                if hand_type == 3:
                    # Full house
                    return 4
                # or if we already found a pair
                if hand_type == 1:
                    # Two pair
                    return 2
                hand_type = 1
        if t == 1:
            if jokers == 4:
                # Five of a kind
                return 6
            if jokers == 3:
                # Four of a kind
                return 5
            if jokers == 2:
                # if we reach here, only one option, 3 different cards and 2 jokers
                # best we can do with this hand is
                # Three of a kind
                return 3
            if jokers == 1:
                # if we reach here, two options :
                # - a pair, 2 different cards and 1 joker
                # - 4 different cards and 1 joker
                if hand_type == 3:
                    # we can't do better, we previously used joker with a pair to build a
                    # Three of a kind
                    return 3
                # joker was not used previously, best we can do with this hand is
                # One pair
                return 1

    return hand_type


print("sample: ", challenge(filename="sample"))
print("input: ", challenge(filename="input"))
