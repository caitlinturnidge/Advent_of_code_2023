"""Advent of code 2023"""
from functools import cmp_to_key


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def create_card_dict(input):
    """Create and return a card dict, with the hand and bet value."""
    ranked = []
    for hand in input:
        rank = {}
        rank['hand'] = hand[:5]
        rank['bet'] = hand[6:].strip('\n')
        ranked.append(rank)
    return ranked


def get_card_value1():
    """Function to get the value of a card."""
    return {
        'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


def get_type_value(hand):
    """Works out the type of hand and returns a value representing the type."""

    hand_list = list(hand)
    hand_list.sort()
    hand = ''.join(hand_list)

    if len(set(hand)) == 1:
        return 7
    elif (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]):
        return 5
    elif len(set(hand)) == 2:
        return 6
    elif (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[1] == hand[2] and hand[3] == hand[4]):
        return 3
    elif len(set(hand)) == 3:
        return 4
    elif len(set(hand)) == 4:
        return 2
    else:
        return 1


def sort_cards1(card1, card2):
    """Sorting function to order the cards in their values and types."""

    card_values = get_card_value1()

    card1_value = card1['hand']
    card2_value = card2['hand']

    card1_type = get_type_value(card1_value)
    card2_type = get_type_value(card2_value)

    if card1_type > card2_type:
        return 1
    elif card1_type < card2_type:
        return -1
    elif card1_type == card2_type:
        for i in range(5):
            if card_values[card1_value[i]] > card_values[card2_value[i]]:
                return 1
            elif card_values[card1_value[i]] < card_values[card2_value[i]]:
                return -1
    return 0


def part_one(input):
    """Sum of all the bid and ranks for all the hands."""
    cards = create_card_dict(input)
    ranked = sorted(cards, key=cmp_to_key(sort_cards1))
    total = 0
    for i, card in enumerate(ranked):
        total += int(card['bet']) * (i+1)
    return total


def get_card_value2():
    """Function to get the value of a card, with special joker"""
    return {
        'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13}


def get_highest_type_value(hand):
    """Works out the highest type of hand, given the joker can be anything and returns a value representing the type."""
    values = get_card_value2()
    highest = 0
    for value in values:
        new_hand = hand.replace('J', value)
        highest_type = get_type_value(new_hand)
        if highest < highest_type:
            highest = highest_type
    return highest


def sort_cards2(card1, card2):
    """Sorting function to order the cards in their values and highest types."""

    card_values = get_card_value2()

    card1_value = card1['hand']
    card2_value = card2['hand']

    card1_type = get_highest_type_value(card1_value)
    card2_type = get_highest_type_value(card2_value)

    if card1_type > card2_type:
        return 1
    elif card1_type < card2_type:
        return -1
    elif card1_type == card2_type:
        for i in range(5):
            if card_values[card1_value[i]] > card_values[card2_value[i]]:
                return 1
            elif card_values[card1_value[i]] < card_values[card2_value[i]]:
                return -1
    return 0


def part_two(input):
    """Sum of all the bid and ranks for all the hands."""
    ranked = create_card_dict(input)
    ranked = sorted(ranked, key=cmp_to_key(sort_cards2))
    total = 0
    for i, card in enumerate(ranked):
        total += int(card['bet']) * (i+1)
    return total


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
