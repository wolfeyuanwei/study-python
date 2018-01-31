#!/usr/bin/python
#filename:enumerate_test.py
#-*- coding: UTF-8 -*-

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
eu = enumerate(seasons)
print type(eu)

for i, season in enumerate(seasons):
    print i, season

for i, season in eu:
    print i, season