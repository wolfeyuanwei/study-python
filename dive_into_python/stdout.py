#!/usr/bin/python
#filename:stdout.py

import sys
print 'Dive in'
saveout = sys.stdout
fsock = open("out.log", 'w')
sys.stdout = fsock
print 'This message will be logged insteda of display'
sys.stdout = saveout
fsock.close()