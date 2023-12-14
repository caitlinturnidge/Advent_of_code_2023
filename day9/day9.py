"""Advent of code 2023"""


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def check_differences(differences):
    """Check that the sequence doesn't have all zeros in it, to stop the while loop."""
    if [] in differences:
        return False
    return any(not all(element == 0 for element in item) for item in differences)


def find_next_number(line):
    """Sum the next numbers in the sequences, for a given line."""
    all_differences = [line]

    while check_differences(all_differences):
        difference = []
        focus = all_differences[-1]
        for i, char in enumerate(focus):
            if i > 0:
                difference.append(
                    int(focus[i]) - int(focus[i-1]))
        all_differences.append(difference)

    total = 0
    for list in all_differences:
        if len(list) > 0:
            total += int(list[-1])
    return total


def part_one(input):
    """Find the next number in all the sequences and sum them."""
    total = 0
    for line in input:
        line = line.strip('\n').split(' ')
        total += find_next_number(line)
    return total


def find_number_before(line):
    """Given the difference sequences, calculate the sum of all the previous numbers for a given line."""
    all_differences = [line]

    while check_differences(all_differences):
        difference = []
        focus = all_differences[-1]
        for i, char in enumerate(focus):
            if i > 0:
                difference.append(
                    int(focus[i]) - int(focus[i-1]))
        all_differences.append(difference)

    differences = all_differences[:-2]
    numbers_before = [0]

    for i in range(len(differences)+2):
        if i > 1:
            numbers_before.append(
                int(differences[len(differences) - i][0]) - numbers_before[-1])

    return -numbers_before[-1]


def part_two(input):
    """Find the number before in all the sequences and sum them."""
    total = 0
    for line in input:
        line = line.strip('\n').split(' ')
        total += find_number_before(line)
    return total


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
