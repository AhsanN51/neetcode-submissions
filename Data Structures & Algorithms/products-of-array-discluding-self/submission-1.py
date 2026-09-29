class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        p=1
        for i in range(len(nums)):
           p*=nums[i]
           pre[i]=p
        p=1 
        for i in range((len(nums)-1),0,-1):
           p*=nums[i]
           suf[i]=p
        r=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                r[i]=suf[i+1]
            elif i==(len(nums)-1):
                r[i]=pre[i-1]
            else:
                r[i]=suf[i+1]*pre[i-1]
        return r