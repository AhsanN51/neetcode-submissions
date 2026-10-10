class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        n=0
        while l<=r:
            n=(l+r)//2
            if (n*n)==x:
                return n
            elif (n*n)<x:
                l=n+1
            else:

                r=n-1
        return r