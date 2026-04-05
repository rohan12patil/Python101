# Find the longest string in a list of strings
# You're given a list of strings.
 
# Your task: Return the length of the longest string in the list.
# Parameters
# the_strings: A list of strings

# Result
# int: The length of the longest string in the list

# Example 1:
# Input: ["Hello", "World", "This is a string"]
# Result: 16
# Want a hint?
# You will need to examine each string in the list.
# You will have to calculate the length of each string.
# You will need to return the length of the longest string.


test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]



def find_largest(strings):
    largest = 0
    for s in strings:
        len(s) > largest
        largest = len(s)

    print(largest)        
    return largest



find_largest(test_strings)