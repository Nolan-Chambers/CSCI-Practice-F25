"""An isolated test of the hangman game logic using hardcoded variables."""

import random
import time


def assign_guess_allowance(difficulty: str) -> int:
    """Determines the number of guesses the user gets depending on their selected difficulty

    Args:
        difficulty (str): the selected difficulty

    Returns:
        int: the number of allotted guesses the user is allowed
    """
    if difficulty == 'easy':
        guesses_allowed = 5
    elif difficulty == 'medium':
        guesses_allowed = 8
    elif difficulty == 'hard':
        guesses_allowed = 10
    else:
        guesses_allowed = 12
    return guesses_allowed


def sort_lists() -> dict:
    """Mimics sorting of data from files, but hardcoded b/c there is no file"""
    easy = ['app', 'bow', 'cow']
    medium = ['apple', 'fired', 'sweater']
    hard = ['conformation', 'independent', 'hypothetical']
    challenge = ['supercalifragilisticexpialidocious', 'hippopotamuses']

    game_words = {easy, medium, hard, challenge}
    return game_words


def random_lvl_choice() -> str:
    """Mimics a user selecting a difficulty level using the random library.
    Returns:
        str: the difficulty level randomly selected
    """
    options = ['easy', 'medium', 'hard', 'challenge']
    choice = random(options)
    return choice

# Or:
def select_level() -> str:
    """Prompts the user to select their desired difficulty level

    Args:
        None

    Returns:
        str: The chosen difficulty
    """
    print("[bold]Difficulty Options:[/bold]" + '\n')
    time.sleep(.5)
    print("[green]Easy[/green]" + " |  " + "[yellow]Medium[/yellow]" + "  | " + "[red]Hard[/red]")
    time.sleep(.5)
    for i in range(3):
        print('.', end='')
        time.sleep(.8)
    print("    [dark_red]Challenge[/dark_red]")
    while True:
        difficulty = input('Enter your desired difficulty level: ').strip().lower()
        if difficulty == 'easy':
            return 'easy'
        elif difficulty == 'medium':
            return 'medium'
        elif difficulty == 'hard':
            return 'hard'
        elif difficulty == 'challenge':
            return 'challenge'
        else:
            print("Please enter a valid difficulty level.")
            time.sleep(0.5)
            continue



def select_word(game_words: dict, choice) -> str:
    """Chooses a random word from the dictionary of lists of words"""
    for words in game_words[f'{choice}']:
        game_word = random(choice)
    return game_word


def guess_and_check(word: str) -> tuple[bool, list]:
    """Checks user input of an individual letter guess

    Args:
        word (str): the word the user is attempting to guess

    Returns:
        tuple[bool, list]: True and a list of the correct letter guesses if correct,
        False and a list of incorrect letters guessed otherwise
    """
    while True:
        letter = str(input().strip().lower())
        if letter.ord() >= 97 and letter.ord() <=122:
            break
        else:
            print("Please enter a valid character.")
            continue

    correct_letters = []  # Will probably be defined in game loop
    incorrect_letters = []  # Ditto
    if letter in word:
        return True, correct_letters.append(letter)
    else:
        return False, incorrect_letters.append(letter)


def chars_guessed(num_guesses: int, word: str, guess: tuple) -> None:
    """Sets up blanks corresponding to the letters in the game word and displays them. Additionally
    fills in the blanks for each guess and displays.
    """
    correct, correct_letters = guess

    if num_guesses == 0:
        print('\n')
        blanks = ' _ ' * len(word)
        print(blanks)
        pass

    if correct:
        print('\n')

        # Will execute for the length of the word
        for char in word:
            # Print letter if guessed
            if char in correct_letters:
                print(char, end=' ')
                # Otherwise print a blank if letter hasn't been guessed yet
            else:
                print('_', end=' ')
    print('\n')
