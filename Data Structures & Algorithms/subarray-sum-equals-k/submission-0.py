class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        dic={0:1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            dif=s-k
            c+=dic.get(dif,0)
            dic[s]=1+dic.get(s,0)
        return c