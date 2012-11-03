

list1 = [1,2,3,4,5,6,7,9,2,4,6]
x = 10
def forLoop():
    global list1
    print "for n in list loop"
    for n in list1:
        print n
    print "For in range loop"
    for k in range(len(list1)):
        print list1[k]

def whileLoop():
    global list1
    global x
    print "while loop"
    while(x > -1):
        print list1[x]
        x= x-1


# call the looping functions
forLoop()
whileLoop()
