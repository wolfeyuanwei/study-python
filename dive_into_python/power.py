#!/usr/bin/python
#filename:power.py
# -*- coding:utf-8 -*-

def my_power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x

    return s

    