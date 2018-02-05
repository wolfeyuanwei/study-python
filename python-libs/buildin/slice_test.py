#!/usr/bin/python
#filename: slice_test.py
#-*- coding: UTF-8 -*-
#实现切片对象

myslice = slice(5)
print myslice
arr = range(10)
print arr
afterslice = arr[myslice]
print afterslice