
import sys
from scrabble.data import LETTER_SCORES
    
def load_word_dictionary(filename):
    """Load words from a file"""

    with open(filename) as f:
        words = f.read().splitlines()
        return(words)

def calc_word_value(word):
    """Calculate the scrabble score of a given word"""

    word_clean = word.upper().replace('-', '')
    scores = [LETTER_SCORES[letter] for letter in word_clean]
    return sum(scores)
    
def max_word_value(word_list):
    """Give the highest scoring word from a list with its score"""
    max_score = 0
    max_score_word = ""
    for word in word_list:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            max_score_word = word
    return (max_score, max_score_word)

def run_part_1(filepath):
    """Read a file and return the highest scoring word with its score"""

    dictionary = load_word_dictionary(filepath)
    max_word = max_word_value(dictionary)
    print(max_word[1] + ': (score ' + str(max_word[0]) + ')')

