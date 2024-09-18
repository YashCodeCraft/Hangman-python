# Hangman Game

Welcome to the Hangman game! This is a simple implementation of the classic game of Hangman in Python.

## Table of Contents

- Installation
- Usage
- Code Overview
- License

## Installation

To run this Hangman game, you'll need to have Python installed on your system. You will also need the `hangman_words` module, which contains a list of words for the game.

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/YashCodeCraft/Hangman-python.git
    cd Hangman-python
    ```

2. **Install dependencies** (if any):
    - For this script, no external packages are required other than the standard Python library.

3. **Create the `list of words` module**:
    - Ensure you have a file named `list of words` in the same directory as your game script.
    - The `list_of_words` file should contain a list of words. For example:
      
      ```python
      words = ["PYTHON", "DEVELOPER", "HANGMAN", "GAME"]
      ```

## Usage

1. **Run the game**:
    ```bash
    python hangman.py
    ```
    - The game will start, and you will be prompted to guess letters. You have 6 lives to guess the word correctly.

2. **Game Instructions**:
    - You will see the current state of the word with dashes (`-`) representing unguessed letters.
    - Input a letter to guess.
    - The game will provide feedback on whether the letter is correct or not.
    - The game ends when you either guess the word correctly or run out of lives.

## Code Overview

Here's a brief overview of the main components of the code:

- **`is_valid_number(words)`**: Selects a random word from the provided list of words and ensures it's a valid word (no dashes or spaces).

- **`hangman()`**: Manages the game logic including user input, updating the word display, and managing the number of lives.

- **`hangman_words.py`**: This file contains the list of words used in the game. Make sure it is present in the same directory as the main game script.




