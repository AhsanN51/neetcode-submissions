class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        n=nums
        for i in range(len(n)):
            if n[i]!=val:
                n[c]=n[i]
                c+=1
        return c