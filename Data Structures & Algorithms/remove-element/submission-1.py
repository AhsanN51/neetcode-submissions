class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p=0
        n=len(nums)-1
        while p<=n:
            if nums[p]==val:
                nums[p]=nums[n]
                n-=1
            else:
                p+=1
        return p