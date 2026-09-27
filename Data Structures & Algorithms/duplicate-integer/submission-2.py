class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ch=[]
        for n in nums:
            if n in ch:
                return True
            ch.append(n) 
        return False