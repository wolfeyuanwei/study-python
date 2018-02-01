#!/usr/bin/python
#filename:issubclass_test.py
#-*- coding: UTF-8 -*-

class A(object):
    pass

class B(A):
    pass


print issubclass(B, A)
print issubclass(B, object)