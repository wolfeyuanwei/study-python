#!/usr/bin/python
#filename: delattr_test.py
# -*- coding: UTF-8 -*-

class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()
print "x = ", point1.x
print "y = ", point1.y
print "z = ", point1.z

delattr(Coordinate, 'z')
print "--删除z属性后--"
print "x = ", point1.x
print "y = ", point1.y
#print "z = ", point1.z