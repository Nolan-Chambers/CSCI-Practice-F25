"""Creates a mock game loop"""

import isolated_test as i_t
from rich import print
import time


def clr_scrn() -> None:
    """Clears the screen. No arguments; returns None.
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def game_options() -> None:
    """Displays a welcome screen and provides options for user to choose from"""

    options = """
 Select An Option:
 ----------------
| 1) [underline]Play[/underline]        |
| 2) [underline]Leaderboard[/underline] |
| 3) [underline]Exit[/underline]        |
 ----------------
    """
    print(options)


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
    





def start_scrn(player_info: list) -> None:
    """Starts program and displays options."""
    clr_scrn()
    print("[green italic]Loading game...[/green italic]")
    for i in range(3):
        time.sleep(0.5)
        print("\n")
    print("[bold]Welcome to Hangman![bold]\n")
    print('[italic[Press ENTER to continue][/italic]')
    input()
    


