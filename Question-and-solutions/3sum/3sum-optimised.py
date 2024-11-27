
# make n3 to n2 time complexity

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort
        triplet = set()
        for i in range(len(nums)):
            list_hash = []
            j = i + 1
            for j in range(i+1,len(nums)):
                # print(f"i = {i}  j = {j}")
                x = - (nums[i]+nums[j])
                if x in list_hash:
                    lst = [x, nums[i], nums[j]]
                    lst2 = lst.sort()
                    triplet.add(tuple(lst))
                list_hash.append(nums[j])
        return list(triplet)


slt = Solution()
print(slt.threeSum([-1,0,1,2,-1,-4]))


