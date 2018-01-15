#!/usr/bin/python
#filename:stderr.py

import sys
fsock = open('error.log','w')
sys.stderr = fsock
raise Exception, "This error will be logged"