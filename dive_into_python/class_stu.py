#!/usr/bin/python
#filename:class_stu.py
# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s:%d' %(self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'


class Animal(object):
    def run(self):
        print 'Animal is running'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

if __name__ == '__main__':
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    #anna = Student('anna', 100);
    #anna.print_score()
    #print anna.name + " got " + anna.get_grade()
    #anna.score = 90
    #print anna.score

    