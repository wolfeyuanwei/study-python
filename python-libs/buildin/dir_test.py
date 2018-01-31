#!/usr/bin/python
#filename:dir_test.py
# -*- coding: UTF-8 -*-

import struct

list = dir() #获得当前模块的属性列表
print list

list1 = dir([]) #查看列表的方法
print list1

attrstruct = dir(struct)
print attrstruct

class Shape(object):
    def __dir__(self):
        return ['area', 'perimeter', 'location']

s = Shape()
objlist = dir(s)
print objlist

