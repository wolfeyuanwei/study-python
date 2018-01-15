#!/usr/bin/python
#filename:pthread_test.py
#-*-coding:utf-8 -*-

import time, threading

def loop():
    print 'thread %s is running...' %threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' %(threading.current_thread().name, n)