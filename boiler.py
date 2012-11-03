

def randFunction():
    print "This function was called from main"


def randFunction2():
    print "This function was called from main as well"

def main():
    print "This boiler plate method forces a main method"
    randFunction()
    randFunction2()



if __name__=='__main__':
    main()
