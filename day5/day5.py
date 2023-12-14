"""Advent of code 2023"""
import re


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def get_next_number(grid_numbers, value) -> int:
    """Get the number after having gone through the grids."""
    rows = [grid_numbers[i:i+3] for i in range(0, len(grid_numbers), 3)]

    for row in rows:
        if int(row[1]) <= value < int(row[1]) + int(row[2]):
            return int(row[0]) + (value - int(row[1]))
    return value


def create_grids(input):
    """Create grids from thw input."""
    grids = []

    grid = []
    for line in input:
        if line == '\n':
            grids.append(grid)
            grid = []
        grid.append(line)
    grids.append(input[170:])

    return grids


def get_seeds(input):
    """Get the starting seeds from the input."""
    seeds_line = input[0][7:]
    return re.findall(r'\b\d+\b', ''.join(seeds_line))


def part_one(input):
    """Get the results of all the starting seeds, and return the smallest one."""
    grids = create_grids(input)
    seeds = get_seeds(input)

    all_results = []
    for seed in seeds:

        for grid in grids[1:]:
            numbers = re.findall(r'\b\d+\b', ''.join(grid))
            seed = get_next_number(numbers, int(seed))

        all_results.append(seed)

    return sorted(all_results)[0]


def get_next_ranges(grid_numbers, values) -> int:
    """Get the final ranges after splitting through the grids."""

    rows = [grid_numbers[i:i+3] for i in range(0, len(grid_numbers), 3)]

    values = set(values)

    ranges = []

    for range_values in values:

        for row in rows:

            if range_values.start < int(row[1]) and range_values.stop < int(row[1]):
                ranges.append(range_values)

            elif range_values.start > int(row[1]) + int(row[2]) - 1 and range_values.stop > int(row[1]) + int(row[2]) - 1:
                ranges.append(range_values)

            elif range_values.start <= int(row[1]) and range_values.stop >= int(row[1]) + int(row[2]) - 1:
                ranges.append(
                    range(range_values.start, int(row[1])))
                ranges.append(
                    range(int(row[0]), int(row[0]) + int(row[2])))
                ranges.append(
                    range(int(row[1]) + int(row[2]), range_values.stop))
                break

            elif range_values.start < int(row[1]) and int(row[1]) < range_values.stop < int(row[1]) + int(row[2]) - 1:
                ranges.append(range(range_values.start, int(row[1])))
                ranges.append(range(int(row[0]), int(
                    row[0]) + (range_values.stop - int(row[1]))))
                break

            elif range_values.start >= int(row[1]) and range_values.stop < int(row[1]) + int(row[2]) - 1:
                ranges.append(range(int(
                    row[0]) + (range_values.start - int(row[1])), int(
                    row[0]) + (range_values.stop - int(row[1]))))
                break

            elif range_values.start >= int(row[1]) and range_values.stop >= int(row[1]) + int(row[2]) - 1:
                ranges.append(range(int(
                    row[0]) + (range_values.start - int(row[1])),
                    int(row[0]) + int(row[2])))
                ranges.append(
                    range(int(row[1]) + int(row[2]), range_values.stop))
                break

            else:
                ranges.append(['error'])

    return ranges


def get_starting_ranges(input):
    """Get the starting ranges"""
    result_ranges = []

    seeds = get_seeds(input)

    values = [int(value) for value in seeds]

    for i in range(0, len(values), 2):
        if i + 1 < len(values):
            start = values[i]
            end = start + values[i + 1]
            result_ranges.append(range(start, end))
    return result_ranges


def part_two(input):
    """Get the results of all the starting seeds, and return the smallest one."""
    grids = create_grids(input)
    values = get_starting_ranges(input)

    final_ranges = []

    for grid in grids[1:]:
        numbers = re.findall(r'\b\d+\b', ''.join(grid))
        values = get_next_ranges(numbers, values)
    final_ranges.append(values)

    smallest = 100000000
    for i in range(len(final_ranges)):
        for j in range(len(final_ranges[i])):
            if final_ranges[i][j] != ['error']:
                if smallest > final_ranges[i][j].start > 35000000:
                    smallest = final_ranges[i][j].start
    return smallest


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
