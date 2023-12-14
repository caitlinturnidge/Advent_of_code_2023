"""Advent of code 2023"""


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def calculate_score(card: str) -> int:
    """Calculates the score of a given scratchcard."""
    score = 0
    card = card.split('|')
    numbers = card[0][9:].split()
    winning_numbers = card[1].split()
    for number in numbers:
        if number in winning_numbers:
            if score == 0:
                score = 1
            else:
                score = score * 2
    return score


def part_one(cards):
    """Sums all the scratchcard scores together."""
    total = 0
    for card in cards:
        score = calculate_score(card)
        total += score
    return total


def get_number_of_wins(card: str) -> int:
    """Get the number of winning numbers on a given scratchcard."""
    score = 0
    card = card.split('|')
    numbers = card[0][9:].split()
    winning_numbers = card[1].split()
    for number in numbers:
        if number in winning_numbers:
            score += 1
    return score


def part_two(input):
    """Calculate the number of scratchcards you end up with."""
    copies = {}

    for i, card in enumerate(input):
        copies[f'card {i+1}'] = 1

    for i, card in enumerate(input):

        copy = copies[f'card {i+1}']
        score = get_number_of_wins(card)

        for j in range(i+1, score+1+i):

            copies[f'card {j+1}'] = copies[f'card {j+1}'] + (copy)

    return sum(copies.values())


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
