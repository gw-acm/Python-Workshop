#! usr/bin/env python

import math

def function(x,y):
    a = math.pow(x,2)
    b = y ** 2
    temp = a + b
    return math.sqrt(temp)

print function(2,2)
print function(3,4)
