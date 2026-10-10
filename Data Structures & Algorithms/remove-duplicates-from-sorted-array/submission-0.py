class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=nums
        p=1
        for i in range(1,len(n)):
            if n[i-1]!=n[i]:
                n[p]=n[i]
                p+=1
        return p