#!/usr/bin/python
#filename: type_test.py
#-*- coding: UTF-8 -*-

print type(1)

print type("python")

print type([1, 2, 3])

print type({0:'zero'})

class X(object):
    a = 1

X = type('X', (object,), dict(a=1))
print X