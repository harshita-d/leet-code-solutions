class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(0)
        for i in range(0,len(nums)+1):
            if i!= nums[i] :
                return i