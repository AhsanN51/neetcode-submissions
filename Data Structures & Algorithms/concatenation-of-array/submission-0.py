class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*2*len(nums)
        n=nums
        for i in range(len(nums)):
            ans[i]=n[i]
            ans[i+len(n)]=n[i]
        return ans