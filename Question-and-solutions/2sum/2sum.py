# Brute Force Solution :

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        #  calculate lenght of nums
        nums_length = len(nums)        

        # blank indices in order to add two element indices which sum == target                                       
        indices = []

        # for loop for length of i to iterate over indices of nums
        for i in range(nums_length):  
            for j in nums :

            #  in short [2,7,11,15]  = here if i == num.index(j) then skip n[0] + j
            #   i =0 n[0] = 2   check (index of 2) == 0 then here 2 + 2 sum skipped
                if i == nums.index(j):                      
                    continue
                target_check = j + nums[i]
                if target_check == target :
                    indices.append(i)
        return indices

myobject = Solution()
ans = myobject.twoSum([3,3],6)

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



