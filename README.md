# Wordle Bot
Wordle Bot is a Python program that helps solve the daily NYT Wordle using only list manipulation. No external libraries or advanced data structures,just pure Python lists, sets, and string operations.

This project was created for fun to explore solving Wordle using only basic Python structures, by someone who admits that they are "just bad at wordle".


Tracks correct letters (green) and potential letters (yellow).
Maintains a list of excluded letters (black).
Suggests the best next guesses based on remaining valid words and letter frequency.
Built entirely with Python lists and sets—no NumPy or other libraries.


Installation
1. Clone the repository:

2. Ensure you have the file valid-wordle-words.txt containing all valid 5-letter words in the same directory.

3. Run the bot (wordle_bot.py)

Usage
   
1. Enter your first guess when prompted.
2. After each guess, input the results using:
  g for green (correct position)
  y for yellow (wrong position)
  b for black/gray (not in the word)

Example input after a guess:

How did your guess do (g - green , y - yellow , b - black): gybgb

3. The bot will update its tracking and suggest the next best guesses.
4. Repeat until the solution is found.
