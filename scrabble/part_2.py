import os
import random
import sys
import itertools

from scrabble.part_1 import load_word_dictionary, calc_word_value, max_word_value
from scrabble.data import POUCH

def get_valid_words(letters, valid_words):
    """Simple First approach. Find all valid words, then score them"""

    valid_words = set(valid_words)

    words = []
    for x in range(len(letters), 0, -1):
        for permutation in itertools.permutations(letters, x):
            word = ''.join(permutation).lower()
            if word in valid_words and word not in words:
                words.append(word)

    return words

def get_optimal_score(draw, valid_words):
    """Find all valida words from draw and return the highest score along with an example word"""
    
    all_words = get_valid_words(draw, valid_words)
    max_value, max_word = max_word_value(all_words)
    
    return max_value, max_word

directory = os.path.dirname(__file__)

def run_part_2():
    #Sample 7 random values from the Pouch
    letters = random.sample(POUCH, 7)
    #Print this value to the user as a string
    print("Your letter:", str(letters))
    #Ask the player for an input - take as capital
    player_word = input("Enter your word:").lower()

    #Validate input: both for using correct letters and valid choice
    letters_remaining = [l.lower() for l in letters]
    
    for idx in range(len(player_word)):
    
        letter = player_word[idx].lower()
    
        if letter in letters_remaining:
            letters_remaining.remove(letter)
        else:
            print("Word given does not use only the letters drawn!")
            sys.exit(1)

    valid_words = load_word_dictionary(directory + '\\dictionary.txt')
    
    if player_word not in valid_words:
        print("Word given is not in list of valid words!")
        sys.exit(1)


    #Calculate the given word value and show it to the player.
    player_word_score = calc_word_value(player_word)
    print("Your: ", player_word, " has score: ", player_word_score)


    #Calculate the optimal word (= max word value) by checking all permutations of the 7 letters of
    #the draw, cross-checking with the set of valid words.
    max_score, max_word = get_optimal_score(letters, valid_words)

    #Give the player the optimal word and its value
    print('Optimal word possible: ', max_word, ' ( value: ', max_score, ')', ) 

    #Give the player their score
    player_score = 100 * (player_word_score / max_score)
    print("Your score: ", player_score)
