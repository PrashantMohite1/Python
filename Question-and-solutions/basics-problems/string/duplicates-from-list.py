"""
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

"""


################# BRUTE FORCE #####################################


# lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# lst1 = [10,20,30,40,10]


# l1 = len(lst1)

# lst1.sort()

# i = 0
# j = 0

# result = []

# for i in range(l1):
#     if i not in result:
#         for j in range(i+1, l1):
#             if lst1[i] == lst1[j]:
#                 result.append(lst1[i])
#                 break


# print(f"Input list = {lst1}")
# print(result)

    
############## Hash Map ############################################

# lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# dic1 = {}

# d2 = { "a": "prashant"}



# for i in lst1 :
#     if i in dic1:
#         dic1[i] += 1
#     else:
#         dic1[i] = 1



# print(dic1)



######### set approach ################


lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

s1 = set()

duplicates = set()


for i in lst1:
    if i in s1:
        duplicates.add(i)
    else:
        s1.add(i)


print("Original List :- ", lst1)

print(f"Unique Elements :- ", s1)

print(f"Duplicate Element ", duplicates)


