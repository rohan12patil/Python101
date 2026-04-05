# Built in Functions


myString = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the builtin len() function calculates the length of a sequence
# print(len(myString))
# print(len(mynumbers))


# the max() and min() fns will find the largest & smallest value in a sequence
# print(max(myString))
# print(min(mynumbers))


# the str() fn will return a string version of an object
prefix = "result: "
result = 5
# print(prefix + result) #this gives error can only concatenate str (not "int") to str
# print(prefix + str(result) )


# range(start, stop, step) will create a range of numbers 
# ranges can be used along with loops
# for i in range(5, 15, 3):
#     print(i)


# for i in range(4, len(myString), 2):
    # print(myString[i])

#String Interpolation : the print function itself is pretty flexible - you can embed variables directly into a string

greeting = "Hello!"
count = 10
print(f"{greeting} you are visitor number {count}")
