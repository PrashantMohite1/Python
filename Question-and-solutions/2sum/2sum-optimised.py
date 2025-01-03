class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)

        dict1 = {}
        lst1 = []

        for i in range(n):
            result = target - nums[i]
            if result in dict1:
                return (dict1[result], i)
            dict1[nums[i]] = i
