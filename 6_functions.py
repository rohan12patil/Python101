# Functions in Python

# Basic Function
# def hello_func():
#     print('Hello World !')
#     name = input("What is your name? ")
#     print("Nice to meet you,",name)


# hello_func()

# function that takes parameters

# def hello_func(greeting):
#     print('Hello World !')
#     name = input("What is your name? ")
#     print(greeting,name)


# hello_func("How are you doing")
# hello_func("Hey what's up")


# function that return a value
# def cube(x):
#     return x*x*x

# result = cube(3)
# print(result)


#function with default value for a parameter

# def hello_func(greeting, name=None):
#     print('Hello World !')
#     if name == None:
#         name = input("What is your name? ")
#     print(greeting,name)


# hello_func("How are you doing","Joe")
# hello_func("Hey what's up")


# function with variable number of parameters

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(10,4,5,10,4))