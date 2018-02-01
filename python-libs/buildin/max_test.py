#!/usr/bin/python
#filename:max_test.py
#-*- coding: UTF-8 -*-

print max(1, 2)
print max(2, 10, 5)
print max('113523')

a = [1, 2]
b = [1, 1]
c = [1, 2]

d = max(a, b ,c)
print d

print max('a', 'c')

print max(1, 2, '3', key = int)