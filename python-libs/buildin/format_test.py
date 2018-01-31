#!/usr/bin/python
#filename:format_test.py
#-*- coding: UTF-8 -*-

print "{} {}".format("hello", "world")

print "{0} {1}".format("hello", "world")
print "{1} {0}".format("world", "hello")

print "姓名：{name}, 网址：{url}".format(name="python 内建函数", url="https://docs.python.org/2/library/functions.html#basestring")

class AssignValue(object):
    def __init__(self, value):
        self.value = value

my_value = AssignValue(12)
print "value为: {0.value}".format(my_value)

print "{:.2f}".format(3.1415926)