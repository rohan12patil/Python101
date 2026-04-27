# Working with Modules
# Import the match Module, which contains features for working with Mathematics

import math

print('Square root of 16 is', math.sqrt(16))

# import a specific part of the module so you can refer to it more easily
from math import pi
print("Pi is : ",pi)

# import a module and give it a different name
import random as r

print(r.randint(100, 200))

#Tabulate 
data = [
    ["Product","Price","Stock"],
    ["Laptop",999,40],
    ["Keyboard",99,20],
    ["Mouse",50,50]
]

# Create a formated table using tabulate
from tabulate import tabulate
print(tabulate(data,headers='Name',tablefmt='fancy_grid'))
