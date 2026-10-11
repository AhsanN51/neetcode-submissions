class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*2*len(nums)
        n=nums
        l=len(n)
        for i in range(len(nums)):
            ans[i]=ans[i+l]=n[i]
        return ans