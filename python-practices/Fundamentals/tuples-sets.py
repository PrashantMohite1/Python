# [] list , () tuple , {} set

# tuple - A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created.

# access items in tuple
# try modifying a tuple - it will raise an error

# //////// set ////////

# a set - {}  : is a collection of unique items. means set elements cannot be duplicated
# we can add mixed data in that - such as int, str, float
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

#  empty set

# set are unordered - that means we cannot access items in a set by index

# add and update item in set.

# set operations - union operation | ,  intersection operation & , difference operation - , symmetric difference operation ^



tup1 = (1,2, 3, 4,5)
print(type(tup1))
print(tup1)

# tup[0] = 10    this will raise an error because tuple is immutable
print(tup1[0])


# //////// set ////////

set1 = {1,2, 3, 4, 5 , 5, 2}   # here you can see repeated elements are not printed

set2 = {"Prashant", 11, "hello", 23}  # here you can see mixed data type elements are printed

print("set1: ", set1)
print("set2 : ", set2)



set1.add(110)

print("set after add : ", set1)

# set1.update(11,22)  this will raise an error because update method takes only takes list, tuple, set, dictionary in arguments
set1.update({11,22})

print("set after update : ", set1)

set3 = {1,2,3,4}
set4 = {2,3, 5,6,7,8}

print("union of set3 and set4 : ", set3 | set4)

print("intersection of set3 and set4 : ", set3 & set4)  # this prints the common elements in both sets

print("difference between set3 and set4 : ", set3 - set4)  # this prints the elements in set3 that are not in set4