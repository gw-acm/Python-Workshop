#! /usr/bin/env python

list1 = [1,2,3,4,5,6,7,8,9,10]
x = 9

def forLoop():
    print "for n in list loop"
    for n in list1:
        print n

    print "For in range loop"
    for k in range(len(list1)):
        print list1[k]
def whileLoop():
    global x
    print "while loop"
    while (x > -1):
        print list1[x]
        x = x - 1

forLoop()
whileLoop()
