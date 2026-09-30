class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=numbers
        l=0
        r=len(n)-1
        while (l<r):
            v=n[l]+n[r]
            if v<target:
                l+=1
            elif v>target:
                r-=1
            if v==target:
                return [l+1,r+1]