#!/usr/bin/python
#filename:getattr_test.py
#-*- coding: UTF-8 -*-

class A(object):
    bar = 1

a = A()
print getattr(a, 'bar')
print getattr(a, 'bar2', 3)
print getattr(a, 'bar2')