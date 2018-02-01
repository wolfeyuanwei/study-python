#!/usr/bin/python
#filename:isinstance_test.py
#-*- coding: UTF-8 -*-

a = 2
print isinstance(a, int)
print isinstance(a, str)

print isinstance(a, (str, int, list))

class A(object):
    pass

class B(A):
    pass

print isinstance(A(), A)
print type(A()) == A
print isinstance(B(), A)
print type(B()) == A