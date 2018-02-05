#!/usr/bin/python
#filename:reduce_test.py
#-*- coding: UTF-8 -*-

def add(x, y):
    return x + y

print reduce(add, [1, 2, 3, 4, 5])

print reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])