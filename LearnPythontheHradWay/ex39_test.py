#!/user/bin/python
#filename:ex39_test.py
#-*-coding:utf-8 -*-

import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '-' * 50
print "NY State has: %s" %hashmap.get(cities, 'NY')
print "OR State has: %s" %hashmap.get(cities, 'OR')

print '-' * 50
print "Michigan's abbreviation is: %s" %hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" %hashmap.get(states, 'Florida')

print '-' * 50
print "Michigan has: %s" %hashmap.get(cities, hashmap.get(states, 'michigan'))
print "Florida has: %s" %hashmap.get(cities, hashmap.get(states, 'Florida'))

print '-' * 50
hashmap.list(states)

print '-' * 50
hashmap.list(cities)

print '-' * 50
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas"