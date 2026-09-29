class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        pre=1
        for i in range(len(nums)):
            r[i]=pre
            pre*=nums[i]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            r[i]*=suf
            suf*=nums[i]
        return r