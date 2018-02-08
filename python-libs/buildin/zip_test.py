#!/usr/bin/python
#filename:zip_test.py
#-*-coding: UTF-8 -*-

a = [1, 2, 3]

b = [4, 5, 6]

c = [4, 5, 6, 7]

zipped = zip(a, b)
print zipped

print zip(a, c)

print zip(*zipped)