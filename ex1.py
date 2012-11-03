#! /usr/bin/env python

thirty = 32.0


def fahren(cent):
    temp = 9.0/5.0
    temp2 = temp *cent
    return temp2 + 32

def centri(fahr):
    temp1 = 5.0/9.0
    temp2 = fahr - 32.0
    return temp1 * temp2

def main():
    strings = raw_input("Please enter fahr or cent")
    print strings
    if strings == 'fahr':
        centigrade = input("Input a centigrade value")
        fahr = fahren(centigrade)
        print fahr
    elif strings == 'cent':
        fahrn == input("Input a fahren value")
        cent = centri(fahrn)
        print cent
        
if __name__=='__main__':
    main() 

