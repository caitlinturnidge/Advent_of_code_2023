"""Advent of code 2023"""


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def get_symbol_positions(input: str) -> list[list]:
    """Get the positions (x,y) of each symbol."""
    positions = []
    for i, line in enumerate(input):
        line = line.strip('\n')
        for j, char in enumerate(line):
            if not char.isnumeric() and char != '.':
                positions.append([i, j])
    return positions


def get_number_positions(input: str) -> list[dict]:
    """Get the positions of all the left most elements of all the numbers."""
    positions = []
    for i, line in enumerate(input):
        line = line.strip('\n')

        for j, char in enumerate(line):

            if line[j:j+3].isnumeric():
                positions.append({'number': line[j:j+3], 'position': [i, j]})

            elif line[j:j+2].isnumeric() and not line[j-1].isnumeric():
                positions.append({'number': line[j:j+2], 'position': [i, j]})

            elif line[j].isnumeric() and not line[j-1].isnumeric():
                positions.append({'number': line[j], 'position': [i, j]})
    return positions


def find_adjacent_numbers(number_positions: list[dict], symbols_positions: list[list]) -> list[str]:
    """Filter the numbers to just get ones adjacent to a symbol."""
    adjacent_numbers = []

    for number in number_positions:
        x = number['position'][0]
        y = number['position'][1]
        length = len(number['number'])
        number = number['number']
        flag = False

        for i in range(-1, length + 1):

            if [x + 1, y + i] in symbols_positions:
                flag = True
            if [x, y + i] in symbols_positions:
                flag = True
            if [x - 1, y + i] in symbols_positions:
                flag = True

        if flag:
            adjacent_numbers.append(number)

    return adjacent_numbers


def part_one(data: list) -> int:
    """Find and sum all the adjacent numbers together."""
    symbols = get_symbol_positions(data)
    numbers = get_number_positions(data)
    adjacents = find_adjacent_numbers(numbers, symbols)

    sum = 0
    for number in adjacents:
        sum += int(number)
    return sum


def get_gear_positions(input: str) -> list[list]:
    """Get the positions (x,y) of each gear symbol."""
    positions = []
    for i, line in enumerate(input):
        line = line.strip('\n')
        for j, char in enumerate(line):
            if char == '*':
                positions.append([i, j])
    return positions


def get_adjacents_to_gear(number_positions, gear_position):
    """Filter the numbers to get the ones adjacent to a specific gear symbol."""

    x = gear_position[0]
    y = gear_position[1]

    adjacent_numbers = []

    for number in number_positions:

        for i in range(-len(number['number']), 2):

            if str(number['position']) == str([x+1, y+i]):
                adjacent_numbers.append(int(number['number']))
            if str(number['position']) == str([x, y+i]):
                adjacent_numbers.append(int(number['number']))
            if str(number['position']) == str([x-1, y+i]):
                adjacent_numbers.append(int(number['number']))

    return adjacent_numbers


def part_two(data: list) -> int:
    """Multiple two numbers together when they are adjacent to a gear, and sum."""
    gears = get_gear_positions(data)
    numbers = get_number_positions(data)

    total = 0

    for gear in gears:
        num = get_adjacents_to_gear(numbers, gear)
        if len(num) == 2:
            total += (int(num[0]) * int(num[1]))
    return total


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
