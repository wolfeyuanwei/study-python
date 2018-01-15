#!/usr/bin/python
#filename:func.py
# -*- coding:utf-8 -*-

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact(5)

name = ['adam', 'LISA', 'barT']

def FirstUper(str):
    return [x[:1].upper()+x[1:].lower() for x in str]

print FirstUper(name)