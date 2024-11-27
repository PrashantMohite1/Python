'''

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        lst1=[]
        result = set()
        nums.sort()     
        # nums = [-1, 0, 1, 2, -1, -4]
        # if sort not used then  we get {(0, 1, -1), (-1, 0, 1), (-1, 2, -1)}
        # if sort used we get {(-1, 0, 1), (-1, 0, 1), (-1, -1, 2)} so here duplicate will easily identify by the set thats
        # sort is the key here to store only unique triple
        print("sorted list of nums ", nums)

        for i in range(len(nums)):                                     # i = 0 to first loop 0 to n : second loop 1 to n : 3rd loop 2 to n 
            for j in range(i+1 , len(nums)):                           
                for k in range(j+1 , len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 :
                        result.add((nums[i],nums[j],nums[k]))
        for i in result:
            lst = list(i)
            lst1.append(lst)
        
        
        return lst1
        
    
obj1 = Solution()
print(obj1.threeSum([-1,0,1,2,-1,-4]))
