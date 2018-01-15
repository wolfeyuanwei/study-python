#!/usr/bin/python
#filename:pickling.py

#import cPickle as p
import pickle as p

shoplistfile = 'shoplist.data'

shoplist=['apple','mango','carrot']

f = open(shoplistfile, 'w')
p.dumps(shoplist, f)
#p.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile)
storedlist=p.load(f)
print(storedlist)