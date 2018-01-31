#!/user/bin/python
#filename:filter_test.py
#-*- coding: UTF-8 -*-

import math

def is_odd(n):
    return n % 2 == 1

def is_three_double(n):
    return n % 3 == 0

def is_sqr(n):
    return math.sqrt(n) % 1 == 0

sqrlist = filter(is_sqr, range(1, 101))
print sqrlist

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print newlist

threelist = filter(is_three_double, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print threelist

