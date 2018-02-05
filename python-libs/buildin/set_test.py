#!/usr/bin/python
#filename:set_test.py
#-*- coding: UTF-8 -*-
#创建一个无序不重复元素集

x = set("google")
y = set("baidu")

print x
print y

print x & y # 交集
print x | y  #并集
print x - y # 差集