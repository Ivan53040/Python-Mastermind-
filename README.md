This repository contains a Python implementation of the classic Mastermind code-breaking game, developed as Assignment 1 for the CSSE7030 course.
In this version of Mastermind, the computer generates a secret key made up of five digits chosen from 1 to 5, and the player has up to ten attempts to guess it. After each guess the game gives feedback using
B (black) to indicate a correct digit in the correct position,
W (white) to indicate a correct digit in the wrong position.
Players can enter guesses in the required format (number,number,number,number,number), ask for a hint after three guesses, view help text, or quit at any time.
The main file (main.py) includes all gameplay logic: generating the board, validating and placing guesses, calculating and displaying feedback, and managing the game loop. Constants such as commands, messages and board formatting are defined in support.py. Randomness is seeded for consistent behaviour in testing and assessment.
This project is designed to demonstrate fundamental Python programming skills including functions, lists, loops, modular code organisation, user input handling, and simple game logic.
