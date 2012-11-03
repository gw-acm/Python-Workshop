#!/usr/bin/env python

fahr=56.0
centi = 24.0

def fahren1(cent):
    temp = 9.0 / 5.0
   # print temp
    temp = temp*cent
    #print temp
    return temp + 32
    
def centigrade(far):
    temp1 = 5.0 / 9.0
    temp2 = far-32.0
    return temp1 * temp2

fahr1 = fahren1(centi)

centi1 = centigrade(fahr)


print fahr 
print  fahr1
print centi 
print  centi1
