import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}



# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    f = open(DICTIONARY)
    l = f.readlines()
    l2=[]
    for i in l:
        l2.append(i.replace("\n",""))
    return l2


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    s = 0
    for i in word:
        s+=LETTER_SCORES[i.upper()]
    return s


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    s_max = 0
    for w in words:
        s_new = calc_word_value(w)
        if s_new > s_max:
            s_max = s_new
            w_max = w
    return w_max

