# Dictionary: a key-value data structure
# Keys have to immutable datatype, unique
mydict = {
    "one" : 1,
    "two" : 2,
    3: "three",
    4.5: ["four","point","five"]
}

# print(mydict)

# dictionaries are accessed via keys
# print(mydict["one"])
# print(mydict[3])

# You can also set dictionary data by creating a new key
# mydict["seven"] = 7;
# print(mydict)

# Trying to access a nonexistent key will produce an error
# print(mydict["bob"])
# print(mydict)

# To avoid this, use 'in' operator to see if key exists
# print("two" in mydict) 
# print("bob" in mydict)


# Retrive all keys & value from a dictionary
# print(mydict.keys())
# print(mydict.values())


# Iterate over all items in dictionary
for key, val in mydict.items():
    print(key,val)