#!/usr/bin/python
#filename:reference.py

print("Simple Assignment")
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print("shoplist is", shoplist)
print("mylist is", mylist)

print("Copy by marking a full slice")
mylist=shoplist[:]
del mylist[0]

print("shoplist is", shoplist)
print("mylist is", mylist)