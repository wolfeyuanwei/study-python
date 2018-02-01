#!/usr/bin/python
#filename: map_test.py
#-*- coding: UTF-8 -*-

def square(x):
    return x ** 2

print map(square, [1, 2,3,4,5])

print map(lambda x: x ** 2, [1, 2, 3, 4, 5])