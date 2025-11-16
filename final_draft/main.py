"""Creates a mock game loop"""

import isolated_test as i_t
import player_file as p_f
from rich import print
import time


def clr_scrn() -> None:
    """Clears the screen. No arguments; returns None.
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def game_options() -> int:
    """Displays a welcome screen and provides options for user to choose from.

    Returns:
        int: the player's selected option
    """

    options = """
 Select An Option:
 ----------------
| 1) [underline]Play[/underline]        |
| 2) [underline]Leaderboard[/underline] |
| 3) [underline]Exit[/underline]        |
 ----------------
    """
    print(options)
    while True:
        selection = int(input('Enter option: ').strip())
        if selection == 1 or selection == 2 or selection == 3:
            return selection
        else:
            print('Please enter a valid option.')
            time.sleep(0.5)
            continue



def hangman_loop(user: str, guesses: int) -> bool:
    """The main game loop

    Args:
        user (str): the username of the player
        guesses (int): the max number of guesses the player gets

    Returns:
        bool: True if the player guesses the word in time, False otherwise
    """
    clr_scrn()
    print("[green italic]Beginning game...[/green italic]")
    time.sleep(0.5)
    print("[Bold]Ready?[/Bold]")
    print('[italic[Press ENTER to continue][/italic]')
    input()
    clr_scrn()

    difficulty = i_t.select_level()
    


def start_scrn() -> None:
    """Starts program and displays options."""
    clr_scrn()
    print("[green italic]Loading game...[/green italic]")
    for i in range(3):
        time.sleep(0.5)
        print("\n")
    print("[bold]Welcome to Hangman![bold]\n")
    print('[italic[Press ENTER to continue][/italic]')
    input()
    

def main() -> None:
    """Main function for the game to operate through"""
    clr_scrn()
    player_data = p_f.sort_player_data(file_name="playerData.yaml")
    if not player_data:
        player_data = []

    start_scrn()
    username = p_f.add_player_data()
    user = p_f.fetch_player_data(player_data, username['Username'])
    if user not in player_data:
        player_data.append(username)
    else:
        username = user

    while True:
        clr_scrn()
        selection = game_options()
        if selection == 1:
            # game
        elif selection == 2:
            # view leaderboard
        elif selection == 3:
            print("[green italic]Saving data...[/green italic]")
            p_f.save_data(file_name="playerData.yaml", player_data=player_data)
            time.sleep(0.5)
            print("[bold]Quitting game.[/bold]")
            input('Press [ENTER] to exit.')
            break


