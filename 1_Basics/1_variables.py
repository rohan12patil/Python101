#Basic variables 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)


# another_str = ' THis is another string'
# print(mystr + another_str)
# print('nom ' * 3)

# Below will cause a error with string 
# print(mystr+1)


# Logical & Comparison Operators

print(myint == 10)
print(myfloat != 20)
print(myint > 20)
print(myfloat < 10)

print(myint > 5 and myfloat < 25.0)
print(myint < 5 or myfloat < 25.0)
print(not (myint < 5 or myfloat < 25.0))

#re-declaring a variable works
myint = "abc"  # changing both value & type
print(myint)