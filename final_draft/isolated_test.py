"""An isolated test of the hangman game logic using hardcoded variables."""

import random

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


def select_word(game_words: dict, choice) -> str:
    """Chooses a random word from the dictionary of lists of words"""
    for words in game_words[f'{choice}']:
        game_word = random(choice)
    return game_word


word = 'apple'

def word_blank_setup(word: str) -> None:
    """Creates the blanks corresponding to the letters in the game word and displays them"""
    blanks = ' _ ' * len(word)
    print(blanks)

# word_blank_setup(word)  # Works!#





def take_guess(word: str) -> tuple[bool, list]:
    """Takes user input for a letter guess"""
    letter = str(input().strip().lower())

    correct_letters = []  # Will probably be defined in game loop
    incorrect_letters = []  # Ditto
    if letter in word:
        return True, correct_letters.append(letter)
    else:
        return False, incorrect_letters.append(letter)

num_guesses = 2  # Will be set in game loop. Defined like in settings of Lab final
guess = (True, ['a', 'p'])
word = 'apple'

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


chars_guessed(num_guesses, word, guess)
