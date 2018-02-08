#!/usr/bin/python
#filename: staticmethod_test.py
#-*- coding: UTF-8 -*-

class C(object):
    @staticmethod
    def f():
        print "staticmethod!!!"

C.f()
cobj = C()
cobj.f()