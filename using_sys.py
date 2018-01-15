#!/usr/bin/python
#FileName:using_sys.py

import sys

print("The Command line arguments are: ")
for i in sys.argv:
    print(i)

print("\n\nThe PYTHONPATH is: ", sys.path, "\n\n")
