# Brute Force Solution :

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #  calculate lenght of nums
        nums_length = len(nums)        

        # created blank indices in order to add two element indices which sum == target                                       
        indices = []

        # for loop for length of i to iterate over indices of nums
        for i in range(nums_length):  
            
            # for loop to iterate over actual values in nums                
            for j in nums:
                if i != nums.index(j):
                    target_check = j + nums[i]
                    if target_check == target :
                        indices.append(nums.index(j))
        return indices
        


myobject = Solution()
ans = myobject.twoSum([2 , 7 , 11 , 15],9)

print(ans)



# Optimised way

nums = [2 , 7 , 11 , 15]
target = 9

indices = []
nums_length = len(nums)



print('list = ', nums)
print("nums length",nums_length)


# for loop for nums then we are checking weather (target-j) is present in list and is list having 2 element.if yes then add index of that list element in indicess
for j in nums:
    target_check = target - j
    if target_check in nums and len(indices) != 2:
        indices.append(nums.index(target_check))
print("indices = ", indices)



