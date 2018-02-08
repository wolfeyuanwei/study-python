#!/usr/bin/python
#filename:vars_test.py
#-*-coding: UTF-8 -*-

print vars()

class Test(object):
    a = 1

print vars(Test)