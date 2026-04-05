# Sequences: Lists and Tuples
#
mylist = [0,1,'two',3.2, False]
# print(len(mylist))
# print(mylist[2])
# print(mylist[4])
# print(mylist)

# Add a list to another list

another_list = [6,7,8]
newlist = mylist + another_list
# print(newlist)

mystr = "This is a string"
# print(mystr[3])
# mystr[2]="Z" #String is immutable

# Use Slice to get parts of sequence
nList = ['a','b','c','d','e','f']
# print(nList[0:4]) # get from index 0 untill 4 not 4th 
# print(nList[1:4:2]) # get from index 1 untill 4 but skip 2
# print(nList[::2])

# you can use slices to reverse a sequence
# print(nList[::-1]) # reverse a string



# Tuples are like lists, but they are immutable they cannot be changed once created 
mytuple = (0,1,2,"three")
print(mytuple)

# Sets are also sequences, but they contain unique values
myset = {1,2,3,4,2}
print(myset) # there are 2 occurances of 2 but they got filter as this is a set

# Sets cannot be indexed like lists or tuples
# print(myset[1]) # this will cause an error

# Set, however, cannot be indexed like lists or tuples

# Test for Membership
print(1 in mylist)
print (3 in mytuple)
print(5 in myset)