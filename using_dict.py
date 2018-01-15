#!/usr/bin/python
#filename:using_dict.py

#'ab' is short for 'a'ddres'b'ook
ab={    'Swaroop'   :   'swaroopch@byteofpython.info',
        'Larry'     :   'larry@wall.org',
        'Matsumoto' :   'matz@ruby-lang.org',
        'Spammer'   :   'spammer@hotmail.com'}

print("Swaroop's address is %s" %ab['Swaroop'])
print("\nThere are %d cantacts in the address-book\n" %len(ab))
#Adding a key/value pair
ab['Guido'] = 'guido@python.org'
print("\nThere are %d cantacts in the address-book\n" %len(ab))

#Deleting a key/value pair
del ab['Spammer']

print("\nThere are %d cantacts in the address-book\n" %len(ab))

for name, address in ab.items():
    print("Contact %s at %s" %(name, address))

if 'Guido' in ab:
    print("\nGuido's address is %s" %ab['Guido'])