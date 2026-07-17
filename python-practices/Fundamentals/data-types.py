'''
list are heterogeneouse means in one list we can store multiple datatypes - int, string, float

In Python, lists are:

Ordered - They maintain the order of elements & index of first item is 0
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.


# List - 
# store different data types 
# access list , specific item 
# remove and add in list 
# slicing - positive (0,1,3,4) and negative. 
#  slicing always walks forward (left to right) by default
# for reverse slice - list[start : stop : step]  list [-1:-7:-1]  here last -1 tells us go in reverse direction

'''


lst1 = [1,23,45,"hello", "prashant"]
print(lst1)

print ("access specific item : ", lst1[0], lst1[3])

lst1.remove(23)
lst1.remove("hello")
print("updated lst after remove : ", lst1)


lst2 = [11,12,13,14,15,16,17]

print("complete list : ", lst2)
print("Slicing 2 - 4  ( here will see last 4th eliment will skip only prints 2nd & 3rd element) : ",lst2[2:4])

print("neghative indexing - (used when want slice from back of the list) ", lst2[1:-3] )
print(lst2[-1 : -8 : -1 ])