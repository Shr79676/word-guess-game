
def make_blank_board(word):
    """Return a list of underscores, one per letter in the word."""
    return ["_" for letter in word]


def reveal_letter(word, board, letter):
    """
    Update board wherever `letter` appears in `word`.
    Return True if the letter was found, False otherwise.
    """
    found = False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            found = True
    return found


def is_word_complete(board):
    """Return True if there are no more underscores left."""
    return "_" not in board
if __name__ == "__main__":
    from words import get_random_word

    word = get_random_word()
    board = make_blank_board(word)
    print("Secret word (for testing):", word)
    print("Board:", " ".join(board))

    reveal_letter(word, board, "o")
    print("After guessing 'o':", " ".join(board))
    print("Complete?", is_word_complete(board))