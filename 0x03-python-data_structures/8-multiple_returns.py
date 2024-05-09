#!/usr/bin/python3
def multiple_returns(sentence):
    lstr = len(sentence)
    if (lstr == 0):
        new_tuple = (lstr, None)
    else:
        new_tuple = (lstr, sentence[0])
    return (new_tuple)
