#!/usr/bin/python
#filename:reload_test.py
#-*- coding: UTF-8 -*-

import sys
print sys.getdefaultencoding()

reload(sys)
print sys.getdefaultencoding()