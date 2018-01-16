#!/usr/bin/python
#filename:ex15.py
#-*-coding:utf-8 -*-

#import package
from sys import argv

#argv unpack
script, filename = argv

#open file with filename
txt = open(filename)

#print filename
print "Here's your file %r:" %filename
#print content which read from file
print txt.read()
#close file
txt.close()
print "Type the filename again: "
#input the filename again
file_again = raw_input(">")
#open file again
txt_again = open(file_again)
#print content again 
print txt_again.read()
txt_again.close()