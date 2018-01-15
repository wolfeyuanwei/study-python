#!/usr/bin/python
#filename:myclass.py
#-*- codeing:utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
    __repr__ = __str__
    def __call__(self):
        print 'My name is %s.' %self.name


class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

if __name__ == '__main__':
    s = Student('Anna')
    print s
    s()
    for n in Fib():
        print n

    f = Fib()
    print 'Fib()[1]: %d' %f[0]