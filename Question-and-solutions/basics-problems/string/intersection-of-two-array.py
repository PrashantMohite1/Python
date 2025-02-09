"""
 Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.

Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not count duplicate elements.

Note: If there is no intersection then return an empty array.

Examples:

Input: arr1[] = [1, 2, 3, 4], arr2[] = [2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are only common elements in both the arrays.

Input: arr1[] = [1, 2, 2, 3, 4], arr2[] = [2, 2, 4, 6, 7, 8]
Output: [2, 4]
Explanation: 2 and 4 are the only common elements.

Input: arr1[] = [1, 2], arr2[] = [3, 4]
Output: []
Explanation: No common elements.

"""


# two pointer approach kaldlka

arr1 = [1, 2, 3, 4,5]
arr2 = [2, 4, 6, 7, 8]

lst1 = []

length = len(arr1)
i = 0
j = 0
while i < len(arr1) and j < len(arr2):
    # print(f"value of i = {i} and value of j = {j}")

    if arr1[i] == arr2[j]:
        print(f"value of i = {i} and value of  j = {j}")
        lst1.append(arr1[i])

        i += 1
        j +=1 

        

    elif arr1[i]< arr2[j]:
        i +=1 

    elif arr1[i] > arr2[j] : 
        j += 1


print("output = ",lst1)