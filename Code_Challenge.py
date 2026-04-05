# Count the number of even or odd numbers in a list
# You're given a list of integers and a string indicating what kinds of numbers to count.
 
# Your task: Count the number of even or odd numbers in the list, based upon the string argument.
# Parameters
# which: A string indicating what kind of numbers to count

# numbers: A list of integers

# Result
# int: The count of the type of numbers in the list (even or odd)

# Constraints
# The numbers list always contains at least one number.
# All numbers in the list will be >= 0.
# The string argument can be anything, so your code needs to check for "even" or "odd" (in lowercase).
# If the which argument is not "even" or "odd", return -1.
# Example 1:
# Input: "even", [2, 5, 20, 30, 55]
# Result: 3
# Example 2:
# Input: "blarg", [20, 30, 55]
# Result: -1
# Want a hint?
# Even numbers are divisible by 2 with no remainder. To perform a division operation that returns the remainder, use the modulo (%) operator.
 

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

# My Solution
def count_numbers(which, numbers):
    # Your code goes here
    evenN = 0
    oddN = 0
    for i, x in enumerate(numbers):
        if (x % 2 == 0 ):
            evenN = evenN + 1
            print('Even found at pos ',i,' is ',x, '    Even Count ',evenN)
        elif (x % 2 == 1):
            oddN = oddN + 1
            print('Odd  found at pos ',i,' is ',x, '    Odd Count ',oddN)
    if(which=="even"):
        return evenN  
    elif(which=="odd"):
        return oddN 
    else: 
        return -1

# Official Solution

# def count_numbers(which, nums):
#     if which !="even" and which != "odd":
#         return -1
    
#     result=0
#     for n in nums:
#         if which == "even" and n % 2 == 0:
#             result += 1
#         if which == "odd" and n % 2 != 0:
#             result += 1
#     return result









result1 = count_numbers("even", numbers)
result2 = count_numbers("odd", numbers)
result3 = count_numbers("Blarg", numbers)


print('Result1 ',result1);
print('Result2 ',result2);
print('Result3 ',result3);