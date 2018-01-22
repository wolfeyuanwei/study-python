#!/user/bin/python
#filename:ex44c.py
#-*-coding:utf-8 -*-

class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORF PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()