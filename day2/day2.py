"""Advent of code 2023"""


def read_input():
    """Get the puzzle input."""
    with open('input.txt', 'r', encoding='utf') as file:
        input = file.readlines()
        return input


def check_game(game: str) -> bool:
    """Checks if the game is valid."""
    for i in range(9, len(game)):
        if game[i-2:i].isnumeric() and int(game[i - 2:i]) > 14:
            return False
        if game[i - 2:i] == '13' and game[i+1] == 'r':
            return False
        if game[i - 2:i] == '14' and game[i+1] == 'r':
            return False
        if game[i - 2:i] == '14' and game[i+1] == 'g':
            return False
    return True


def get_valid_ids(input_list: list) -> list:
    """Return a list of the valid game IDs."""
    valid = []
    for game in input_list:
        stripped_game = game.split(' ')
        game_id = stripped_game[1].strip(':')
        if check_game(game):
            valid.append(game_id)
    return valid


def sum_ids(input_list: list) -> int:
    """Add the numbers in the ID list"""
    sum = 0
    for number in input_list:
        sum += int(number)
    return sum


def get_min_values(game) -> dict:
    """Get and return the max values of each color for a game."""

    values = {'red': 0, 'blue': 0, 'green': 0}

    for i in range(9, len(game)):

        if game[i-2:i].isnumeric() and game[i+1] == 'r':
            if values['red'] < int(game[i-2:i]):
                values['red'] = int(game[i-2:i])

        if game[i-2] == ' ' and game[i-1].isnumeric() and game[i+1] == 'r':
            if values['red'] < int(game[i-1]):
                values['red'] = int(game[i-1])

        if game[i-2:i].isnumeric() and game[i+1] == 'g':
            if values['green'] < int(game[i-2:i]):
                values['green'] = int(game[i-2:i])
        if game[i-2] == ' ' and game[i-1].isnumeric() and game[i+1] == 'g':
            if values['green'] < int(game[i-1]):
                values['green'] = int(game[i-1])

        if game[i-2:i].isnumeric() and game[i+1] == 'b':
            if values['blue'] < int(game[i-2:i]):
                values['blue'] = int(game[i-2:i])

        if game[i-2] == ' ' and game[i-1].isnumeric() and game[i+1] == 'b':
            if values['blue'] < int(game[i-1]):
                values['blue'] = int(game[i-1])

    return values


def get_power(input_list) -> int:
    """Multiple the min values for each game and sum these together."""
    sum = 0
    for game in input_list:
        min_dict = get_min_values(game)
        sum += min_dict['red'] * min_dict['blue'] * min_dict['green']
    return sum


if __name__ == "__main__":
    text = read_input()
    ids = get_valid_ids(text)
    print(f'Part 1: {sum_ids(ids)}')
    print(f'Part 2: {get_power(text)}')
