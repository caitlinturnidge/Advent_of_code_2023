"""Advent of code 2023"""


def read_input():
    """Get the puzzle data."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def get_two_digit_number(string: str):
    """Return the two digit number in the string."""
    numbers = ''
    for char in string:
        if not char.isalpha():
            numbers += char

    if len(numbers) == 1:
        return int(numbers + numbers)

    if len(numbers) == 0:
        return 0

    return int(numbers[0] + numbers[(len(numbers)-1):])


def part_one(data):
    """Add all the two digit numbers from each row."""
    total = 0
    for row in data:
        row = row.strip('\n')
        number = get_two_digit_number(row)
        total += number
    return total


def edit_string(string):
    """replace all the string numbers with actual numbers."""
    check = ''
    for char in string:
        check += char
        if 'one' in check:
            check = check.replace('one', '1')
        if 'two' in check:
            check = check.replace('two', '2')
        if 'three' in check:
            check = check.replace('three', '3')
        if 'four' in check:
            check = check.replace('four', '4')
        if 'five' in check:
            check = check.replace('five', '5')
        if 'six' in check:
            check = check.replace('six', '6')
        if 'seven' in check:
            check = check.replace('seven', '7')
        if 'eight' in check:
            check = check.replace('eight', '8')
        if 'nine' in check:
            check = check.replace('nine', '9')
    return check


def part_two(data):
    """Add the two digit numbers from each row."""
    total = 0
    for row in data:
        row = row.strip('\n')
        new_row = edit_string(row)
        number = get_two_digit_number(new_row)
        total += number
    return total


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
