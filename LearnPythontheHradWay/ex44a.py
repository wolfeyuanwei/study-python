#!/user/bin/python
#filename:ex44a.py
#-*-coding:utf-8-*-
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()