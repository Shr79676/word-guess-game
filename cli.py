from words import get_random_word
from game import make_blank_board, reveal_letter, is_word_complete
from storage import save_score, get_top_scores

MAX_WRONG_GUESSES = 6


def play_round():
    """Play one full round of the guessing game. Return points earned."""
    word = get_random_word()
    board = make_blank_board(word)
    guessed_letters = []
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES and not is_word_complete(board):
        print()
        print("Word:", " ".join(board))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print("You already tried that letter.")
            continue

        guessed_letters.append(letter)
        found = reveal_letter(word, board, letter)

        if not found:
            wrong_guesses += 1
            print("Nope, not in the word.")

    if is_word_complete(board):
        print()
        print("You got it! The word was:", word)
        points = 100 - (wrong_guesses * 10)
        return points
    else:
        print()
        print("Out of guesses. The word was:", word)
        return 0


def main():
    print("=== Word Guess Game ===")
    name = input("Enter your name: ")

    points = play_round()
    print(f"You scored {points} points.")

    save_score(name, points)

    print()
    print("Top scores:")
    for entry in get_top_scores():
        print(f"{entry['name']}: {entry['points']}")


if __name__ == "__main__":
    main()