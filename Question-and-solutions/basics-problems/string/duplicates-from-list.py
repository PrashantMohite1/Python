"""
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]

"""


################# BRUTE FORCE #####################################


# lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

lst1 = [10,20,30,40,10]


l1 = len(lst1)

lst1.sort()

i = 0
j = 0

result = []

for i in range(l1):
    if i not in result:
        for j in range(i+1, l1):
            if lst1[i] == lst1[j]:
                result.append(lst1[i])
                break


print(f"Input list = {lst1}")
print(result)

    



