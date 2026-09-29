class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        maxl=0

        for n in nums:
            if n not in dic:
                left =dic.get(n-1,0)
                right =dic.get(n+1,0)

                l=left+right+1

                dic[n]=l
                dic[n-left]=l
                dic[n+right]=l
                maxl=max(maxl,dic[n])
        return maxl