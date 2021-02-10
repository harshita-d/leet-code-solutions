class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print(len(set(nums)),len(nums))
        x=len(set(nums))
        y=len(nums)
        p=(lambda x,y:False if (x==y) else True)
        return p(x,y)