# Problem Statement

Learning programming and computer science vocabulary can be tedious for beginners when done through repetition and flashcards alone. This project addresses that by turning vocabulary practice into an interactive word-guessing game, making the learning process more engaging.

# Scope

This project is a command-line word-guessing game where the player guesses letters one at a time to reveal a hidden technical/programming term, within a limited number of wrong guesses. The system tracks the player's score based on performance and maintains a persistent leaderboard across sessions using file-based storage.

# Target Users

Beginner programmers, students, and anyone looking to reinforce technical vocabulary in a fun, low-pressure, game-based format.

# High-Level Features

- Word-guessing gameplay with a limited number of wrong guesses (maximum 6 per round)
- Score awarded based on the number of wrong guesses used
- Persistent leaderboard saved to a JSON file, so scores carry over between sessions
- Menu-driven command-line interface allowing the player to play a round, view top scores, or exit
- Modular codebase separating game logic, word data, storage, and the user interface