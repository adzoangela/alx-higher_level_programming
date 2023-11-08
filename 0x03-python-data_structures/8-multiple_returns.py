#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sentence_length = len(sentence)
    else:
        sentence_length = 0
    return (sentence_length, sentence if not sentence else sentence[:1])
