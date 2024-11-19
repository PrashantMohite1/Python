class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = []
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                target_check= nums[i] + nums[j] 
                if target_check == target:
                    return [i, j]
        return [] 
    
myobject = Solution()
ans = myobject.twoSum([3,3,2,2],6)

print(ans)
