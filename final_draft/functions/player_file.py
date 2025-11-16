"""Module for most helper functions of the game."""

import yaml

def save_data(file_name: str, player_data: list) -> None:
    """Writes player data to a yaml file.

    Args:
        file_name (str): the file to write to
        player_data (list): the player's information
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(player_data, file)


def sort_player_data(file_name: str) -> list[dict]:
    """Reads the data from the yaml file and returns it as a list of
    dictionaries.

    Args:
        file_name (str): the file being read

    Returns:
        list[dict]: player information
    """
    player_data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        player_data = yaml.safe_load(file)
    return player_data


def add_player_data() -> dict[str]:
    """Prompts the player for a usename and organizes it into a dictionary.

    Returns:
        dict[str]: the player's username, a count of their correct/incorrect guesses,
        starting at 0, and the total number of games they've played
    """
    user = input("Enter a username: ").strip()
    return {'Username': user, 'Games played': 0, 'Correct guesses': 0, 'Incorrect guesses': 0}


def fetch_player_data(player_data: list, user: str) -> dict[str, int] | None:
    """Finds existing players in the yaml file and pulls their stored
    information.

    Args:
        player_data (list): the list containing the player's data sorted into dictionaries
        user (str): the username of the player

    Returns:
        dict: the player's username and number of correct/incorrect guesses
    """
    for player in player_data:
        if player['Username'] in player_data and player['Username'] == user:
            return player
        else:
            return None
