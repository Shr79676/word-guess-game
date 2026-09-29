from game import make_blank_board, reveal_letter, is_word_complete


def test_make_blank_board():
    assert make_blank_board("cat") == ["_", "_", "_"]


def test_reveal_letter_found():
    board = ["_", "_", "_"]
    found = reveal_letter("cat", board, "a")
    assert found == True
    assert board == ["_", "a", "_"]


def test_reveal_letter_not_found():
    board = ["_", "_", "_"]
    found = reveal_letter("cat", board, "z")
    assert found == False


def test_is_word_complete():
    assert is_word_complete(["c", "a", "t"]) == True
    assert is_word_complete(["c", "_", "t"]) == False


test_make_blank_board()
test_reveal_letter_found()
test_reveal_letter_not_found()
test_is_word_complete()
print("All tests passed!")