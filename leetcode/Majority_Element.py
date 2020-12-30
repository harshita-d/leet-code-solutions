class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return sorted(nums)[len(nums)//2]
        c=0
        t=[nums[0]]
        for i in nums:
            if i==t:
                c=c+1
            elif c==0:
                t,c=i,1
            else:
                c -=1
        return t
                
                
                
            
        