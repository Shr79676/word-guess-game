import random

WORD_BANK = [
    "python", "keyboard", "variable", "function", "computer",
    "loop", "string", "syntax", "module", "developer",
    "array", "boolean", "compiler", "database", "algorithm",
    "network", "software", "hardware", "internet", "operator"
]


def get_random_word():
    """Return one random word from the word bank, in lowercase."""
    word = random.choice(WORD_BANK)
    return word.lower()


if __name__ == "__main__":
    print(get_random_word())