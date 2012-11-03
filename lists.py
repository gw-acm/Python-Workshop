
# create two lists
list1 = [4, 3, 6, 1, 10, 2, 5, 9, 8, 7]
list2 = []

#lets add a data element to the list
list1.append(11)

# lets add multiple elements to the list
list2[0:5] = [2,3,4,5,6,4]


#lets sort out the elements of the lists
list1.sort()
list2.sort()

print list1
print list2

#lets create a new list and store the combined values of list1 and list2
list3 = list1+list2

print list3


#we should probably sort them out, right?
list3.sort()
print list3


# we can also create a list from a subsection of a list
# this takes out the values from index 4 until 6
list4= list3[4:7]

print "list4"
print list4



# side note:this trick also works on strings

string1 = "My name is Lucas"
print string1[3:8]



