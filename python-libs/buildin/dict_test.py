#!/usr/bin/python
#filename:dict_test.py
# -*- coding: UTF-8 -*-

d = dict() #创建空字典
print d

d1 = dict(a='a', b='b', t='t') #参数传入关键字
print d1

d2 = dict(zip(['one', 'two', 'three'], [1, 2, 3])) #映射函数方式构造字典
print d2

d3 = dict([('one', 1), ('two', 2), ('three', 3)]) #可迭代对象方法构造字典
print d3
