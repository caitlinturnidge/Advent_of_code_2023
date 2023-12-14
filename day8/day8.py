"""Advent of code 2023"""
from math import gcd


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def get_elements_dict(maps):
    """Create an element dict, with its left and right values."""
    elements = []
    for row in maps:
        elements.append({'element': f'{row[:3]}',
                         'left': f'{row[7:10]}',
                         'right': f'{row[12:15]}'})
    return elements


def get_next_value(maps, element, rule) -> list[dict]:
    """Get the next value in the sequence, given and element and a rule."""
    elements = get_elements_dict(maps)
    for char in elements:
        if char['element'] == element:
            if rule == 'L':
                return char['left']
            if rule == 'R':
                return char['right']


def part_one(input) -> int:
    """Count the number of steps to reach the element ZZZ."""
    instruction_list = input[0].strip('\n')
    maps = input[2:]
    element = 'AAA'

    steps = 0
    while element != 'ZZZ':
        for instruction in instruction_list:
            element = get_next_value(maps, element, instruction)
            steps += 1
    return steps


def get_starting_elements(maps):
    """Get the starting elements for part 2, elements with an A in them."""
    elements = []
    for row in maps:
        if 'A' in row[:3]:
            elements.append(row[:3])
    return elements


def count_steps(instructions, maps, element) -> int:
    """Count the number of steps to reach an element with Z for a given element."""
    count = 0
    while 'Z' not in element:
        for instruction in instructions:
            element = get_next_value(maps, element, instruction)
            count += 1
    return count


def part_two(input) -> int:
    """Find the lowest common multiple of all the counts of the starting elements."""
    instruction_list = input[0].strip('\n')
    maps = input[2:]
    elements = get_starting_elements(maps)

    counts = []
    for element in elements:
        count = count_steps(instruction_list, maps, element)
        counts.append(count)

    lcm = 1
    for i in counts:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
