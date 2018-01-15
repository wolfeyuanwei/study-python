#!/usr/bin/python
#filename:try_except.py

import sys

try:
    s = input("Enter something -->")
except EOFError:
    print("\nWhy did you do an WOF on me?\n")
    sys.exit()
except:
    print("\nSome error/exception occurred.")

print ("Done")