#!/user/bin/python
#filename:lexicon.py
#-*-coding:utf-8-*-

def scan(sentence):
    results = []
    words = sentence.split(' ')
    for word in words:
        result = ('direction', word)
        results.append(result)
    return results