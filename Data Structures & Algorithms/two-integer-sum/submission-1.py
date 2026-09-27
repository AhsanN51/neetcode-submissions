class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        i=0
        while (a<len(nums)):
            if a==i:
                i+=1
                continue
            if (nums[a]+nums[i]== target):
                return [a,i]
            i+=1
            if (i==len(nums)):
                i=0
                a+=1
