class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=None
        v1=v2=0
        for n in nums:
            if n==c1:
                v1+=1
            elif n==c2:
                v2+=1
            elif v1==0:
                c1,v1=n,1
            elif v2==0:
                c2,v2=n,1
            else:
                v1-=1
                v2-=1
        return [c for c in (c1,c2) if nums.count(c)>(len(nums)//3)]