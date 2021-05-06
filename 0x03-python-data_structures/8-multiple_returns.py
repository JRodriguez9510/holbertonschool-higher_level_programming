#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        t = (len(sentence), None)
        return t
    else:
        t = (len(sentence), sentence[0])
        return t
