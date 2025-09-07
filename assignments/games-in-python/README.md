
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and random selection. By completing this assignment, you will strengthen your ability to work with user input and control program flow.

## 📝 Tasks

### 🛠️\tHangman Game Logic

#### Description
Create a Hangman game where the player tries to guess a hidden word by suggesting letters within a limited number of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Display the word as underscores (e.g., `_ _ _ _`) and update as correct letters are guessed
- Accept user input for letter guesses
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts run out
- Show a win or lose message at the end

**Example:**
```plaintext
Word: _ _ _ _ _
Guess a letter: a
Word: a _ _ _ _
Incorrect guesses left: 5
...
```

### 🛠️\tUser Experience Improvements

#### Description
Enhance the game to make it more user-friendly and visually clear.

#### Requirements
Completed program should:

- Prevent repeated guesses of the same letter
- Show all guessed letters so far
- Handle both uppercase and lowercase input
- Provide clear instructions and feedback to the player

**Example:**
```plaintext
Guessed letters: a, e, t
Please enter a new letter:
```
