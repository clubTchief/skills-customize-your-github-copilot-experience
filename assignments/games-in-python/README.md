
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic word-guessing game using Python strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game State

#### Description
Initialize the word and variables needed to track the player's guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from the predefined list
- Initialize the list of guessed letters
- Set the maximum number of incorrect guesses
- Display the secret word as underscores before any letters are guessed, using spaces such as `_ _ _`

### 🛠️ Process Player Guesses

#### Description
Create a game loop that accepts one letter at a time and updates the game state after each guess.

#### Requirements
Completed program should:

- Prompt the player to enter a letter
- Show the current progress with each correctly guessed letter revealed
- Track letters that have been guessed
- Track incorrect guesses and show how many attempts remain
- Handle a repeated guess without treating it as a new incorrect guess

### 🛠️ Finish the Game

#### Description
End the game when the player guesses the word or exhausts all attempts, then display a clear result.

#### Requirements
Completed program should:

- Continue until the word is fully guessed or no attempts remain
- Display a win message when the player guesses the word
- Display a lose message and reveal the secret word when the player runs out of attempts
