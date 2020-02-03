# Scrabble Game Challenge 

A simple python package to play scrabble that contains the following:

1. A script to calculate the highest scrabble score form a list of words in a text file. 
2. Extention of this code to build up a simple Scrabble-like game on the command line. 

# Part 1

Write a script to read in a series of words from a text file and output the word with the highest 
Scrabble score, along with the score value. The input text file has one word per line.  

### Note:

1. Core data values such as `LETTER_SCORES` are included in the `data.py` file.

2. Make sure the script is executable over the command line and takes the name of the file as the first 
and only command line argument. 

3. A file `dictionary.txt` is included to test upon. 

As you write the code, think about how you may be able to breakdown the problem into a series of tasks, 
and then write a function for each task. e.g. include:

* `load_word_dictionary(filename)` - Given a file name and returns a list of words
* `calc_word_value(word)` - Given a word, return its scrabble score
* `max_word_value(word_list)` - Given a list of words, return a tuple of (score, word) for the highest scoring word. 


# Part 2 

Using what we've coded, we now build a simple Scrabble-like game whereby the user is given a random 
set of 7 letters, and asked to build the most valuable word. 

Users should interact with the script via the command line, with an example session running something like: 

``` 
Letters drawn: G, A, R, Y, T, E, V
Form a valid word: gary  << user input
Word chosen: GARY (value: 8)
Optimal word possible: GARVEY (value: 13)
You scored: 61.5
```

The final score should be based on: 

    (score_achieved / maximum_possible) * 100 


### Steps 

The final program should perform the following steps:

1. Load in any necessary data structures either previously created or stored in `data.py`

2. Draw 7 random letters from the `POUCH` variable. This contains a list of letters with frequencies
 equal to those in scrabble (increased frequencies of vowels etc.). 

3. Ask the player to form a word with one or more of the 7 letters of the draw.  

4. Validate input for:

    1. all letters of word are in those that are drawn;
    2. word is in the given dictionary of allowed words.

5. Calculate the given word value and show it to the player.

6.  Calculate the optimal word (= max word value) by checking all permutations of the 7 letters of 
the draw, cross-checking with the set of valid words.

7. Show the player what the optimal word and its value is.

6. Calculate the players score, then display it. 


# Part 3 

Now we have a working program that is runnable as a series of scripts, the next stage is to package it up so it can be installed. 

Your task is to restructure the scripts into a Python pacakge and refactor the code so that you can run if from within a python session e.g. for part 1:

```
from scrabble.part1 import run_part1

run_part1(words='path/to/word/list.txt')
```

and for part 2

```
from scrabble.part2 import run_part2

run_part2()
```

