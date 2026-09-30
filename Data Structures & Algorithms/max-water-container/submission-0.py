class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=heights
        maxp=0
        p=1
        l=0
        r=len(n)-1
        while (l<r):
            m=min(n[l],n[r])
            p=m*(r-l)
            maxp=max(maxp,p)
            if n[l]<n[r]:
                l+=1
            else:
                r-=1
        return maxp