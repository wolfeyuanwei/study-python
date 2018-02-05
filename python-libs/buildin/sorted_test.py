#!/usr/bin/python
#filename:sorted_test.py
#-*- coding: UTF-8 -*-

a = [5, 7, 6, 3, 4, 1, 2]
print a
b = sorted(a)
print b

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
sortedL = sorted(L, cmp=lambda x, y:cmp(x[1], y[1]))   #利用cmp函数
print sortedL

sortedLL = sorted(L, key=lambda x:x[1])         #利用Key
print sortedLL

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print students

sortedStu = sorted(students, key=lambda s: s[2])
print sortedStu

sortedStuD = sorted(students, key=lambda s: s[2], reverse=True)     #按降序
print sortedStuD