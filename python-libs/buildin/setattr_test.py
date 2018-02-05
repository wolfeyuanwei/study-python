#!/usr/bin/python
#filename: setattr_test.py
#-*- coding: UTF-8 -*-

class A(object):
    bar = 1

a = A()
print getattr(a, 'bar')

setattr(a, 'bar', 10)
print a.bar