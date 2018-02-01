#!/usr/bin/python
#filename:hasattr_test.py
#-*- coding: UTF-8 -*-

class Coordinate:
    x = 10
    y = -5
    z = 0

point = Coordinate()
print hasattr(point, 'x')
print hasattr(point, 'y')
print hasattr(point, "z")
print hasattr(point, 'no')