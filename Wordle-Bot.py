#!/usr/bin/env python
# coding: utf-8

# Wordle Helper Bot
# 
# A simple Python bot to assist with playing Wordle. 
# 
# Instructions:
# - Enter your guess when prompted.
# - For each letter in your guess, input the result as:
#     g = green (correct position)
#     o = orange (wrong position but in the word)
#     b = black (not in the word)
# The bot will suggest the next best guesses to choose from

# In[1]:


import string

def Wordle_Helper(guess, excluded_letter_list, confirmed_letters, potential_letters):
    
    '''
    Processes a 5 letter Wordle guess and returns the best next guesses
    
    Parameters: 
    
    - guess: str, the users current guess
    - excluded_letter_list: set, letters known to not exist in the solution
    - confirmed_letters: list, letters in confirmed postions (green)
    - potential_letters: list, letters in the solution not in correct position (yellow)
    
    
    Returns: 
    
    - updated excluded_letter_list, confirmed_letters,potential_letters
    
    '''
    guess = list(guess)
    
#     Load valid wordle words
    
    with open("valid-wordle-words.txt", "r") as f:
        words = [line.strip() for line in f]
    
    guess_word_list = []

#     User provides their response
    response = input("How did your guess do (g - green , y - yellow , b - black): ").strip().lower()
    
    
#     Processing green and yellow letters
    for i in range(5):
        
        if response[i] == 'g':
            confirmed_letters[i] = guess[i]
            
        elif response[i] == 'y':
            potential_letters.append((guess[i] , i))
        else :
            pass
        


    excluded_letters = set()
    for i, letter in enumerate(guess):
        if response[i] == 'b':
            # only exclude if it wasn't green or orange elsewhere in this guess
            if letter not in [guess[j] for j in range(5) if response[j] in ('g','y')]:
                excluded_letters.add(letter)

    
    excluded_letter_list.update(excluded_letters)
    

#     filtering valid words
    for word in words: 
        word_letters = list(word.lower())

        # must match confirmed green letters
        if any(confirmed_letters[i] != "" and word_letters[i] != confirmed_letters[i] for i in range(5)):
            continue
        
       
        yellow_ok = True
        for (letter, bad_index) in potential_letters:
            if letter not in word_letters:  
                yellow_ok = False
                break
            if word_letters[bad_index] == letter:  
                yellow_ok = False
                break
        if not yellow_ok:
            continue

        # check this guess's green condition
        match = all(
            (word_letters[i] == guess[i] if response[i] == 'g' else True) for i in range(5))

        # must not include excluded letters
        if match and not any(letter in word_letters for letter in excluded_letter_list):
            guess_word_list.append(word)
    
     # Score words based on letter frequency
    letter_count = dict(zip(string.ascii_lowercase , [0]*26))
    for word in guess_word_list:
        for letter in word.lower():
            letter_count[letter] += 1
    
    letter_weights = {letter: freq for letter, freq in letter_count.items()}
    ranked_word_scores = [] 
    for word in guess_word_list: 
        score = sum(letter_weights[letter] for letter in word)
        ranked_word_scores.append(score)   

    sorted_words = sorted(zip(guess_word_list, ranked_word_scores), key=lambda x:x[1], reverse=True)
    unique_letter_words = [(word, score) for word, score in sorted_words if len(set(word.lower())) == len(word)]
    
    print("Here are some of the next best answers:", [word for word, score in unique_letter_words[:10]])
    return excluded_letter_list, confirmed_letters, potential_letters


def Wordle_Bot():
    """
    Main function to run the Wordle bot.
    """
    first_guess = input("What is your starter word:\t")
    
    excluded_letter_list = set()
    confirmed_letters = [""] * 5
    potential_letters = []
    
    # First guess
    excluded_letter_list, confirmed_letters, potential_letters = Wordle_Helper(
        first_guess, excluded_letter_list, confirmed_letters, potential_letters)
    
    # Next guesses
    for attempt in ["second", "third", "fourth"]:
        next_guess = str(input(f"Please give your {attempt} guess: "))
        excluded_letter_list, confirmed_letters, potential_letters = Wordle_Helper(
            next_guess, excluded_letter_list, confirmed_letters, potential_letters)
        
Wordle_Bot()


# In[ ]:




