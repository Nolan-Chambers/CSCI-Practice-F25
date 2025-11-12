

def read_file() -> dict:
    """Reads the text file and sorts the words into lists corresponding to
    their difficulty/length.

    Returns:
        dict: contains four lists of strings sorted
        by difficulty

    """
    words = []
    with open('words.txt', 'r') as opened_file:
        for line in opened_file:
            words.append(line.strip().split())
    opened_file.close()

    easy = []
    medium = []
    hard = []
    challenge = []
    for word in words:
        if len(word) >= 21:
            challenge.append(word)
        elif len(word) >= 15 and len(word) <= 20:
            hard.append(word)
        elif len(word) >= 9 and len(word) <= 14:
            medium.append(word)
        elif len(word) <= 8:
            easy.append(word)
    
    game_words = {}
    game_words.add(easy)
    game_words.add(medium)
    game_words.add(hard)
    game_words.add(challenge)
    return game_words


def select_word(game_words: dict, choice: str) -> str:
    """
    """
