"""Advent of code 2023"""
import re


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def count_wins(time, distance):
    """Count the number of wins for a given time and distance."""
    win_count = 0
    for i in range(int(time)):
        hold_button = i
        time_left = int(time) - hold_button
        if time_left * hold_button > int(distance):
            win_count += 1
    return win_count


def part_one(text):
    """Calculate the number of wins of each race, and multiply them together."""
    times = re.findall(r'\b\d+\b', text[0])
    times = [int(num) for num in times]

    distances = re.findall(r'\b\d+\b', text[1])
    distances = [int(num) for num in distances]

    total = 1
    for i in range(len(times)):
        count = count_wins(times[i], distances[i])
        if count != 0:
            total = total * count

    return total


def part_two(text):
    """Calculate the number of when all the digits are joined together."""
    times = [char for char in text[0] if char.isdigit()]
    distances = [char for char in text[1] if char.isdigit()]
    time = ''.join(times)
    distance = ''.join(distances)
    return count_wins(time, distance)


if __name__ == "__main__":
    text = read_input()
    print(f'Part 1: {part_one(text)}')
    print(f'Part 2: {part_two(text)}')
