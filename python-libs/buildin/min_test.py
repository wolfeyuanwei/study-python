#!/usr/bin/python
#filename:min_test.py
#-*- coding: UTF-8 -*-

print min(1, 1.1, 1.3e1)

print min([2, 3], [2, 2])

print min(1, 2, '3', key=int)