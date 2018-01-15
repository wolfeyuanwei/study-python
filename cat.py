#!/usr/bin/python
#filename:cat.py

import sys

def readfile(filename):
    '''Print a file to standard output'''
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break;
        print(line)

    f.close()

if len(sys.argv) < 2:
    print("No action specified!")
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    if option =='version':
        print("Version 1.2")
    elif option=='help':
        print('\
        The program prints files to the standard output.\n\
        Any number of files can be specified.\n\
        Option include:\n\
            --version: prints the version number\n\
            --help:     Display the help\n')
    else:
        print("Unknown option.")
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)