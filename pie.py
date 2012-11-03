
import sys


def printOut():
    global pie1
    global color
    global language
    print "Hello "+ sys.argv[1]
    print "Your favorite kind of pie is "+ pie1
    print "Your favorite color is " + color
    print "Your favorite programming language is " + language
    print "Haha a "+ color+ " "+pie1+" must be your favorite!!!"   





pie1 = raw_input("Please input your favorite kind of pie: ")
color = raw_input("Please input your favorite color: ")
language = raw_input("What's your favorite programming language? ")

printOut()
