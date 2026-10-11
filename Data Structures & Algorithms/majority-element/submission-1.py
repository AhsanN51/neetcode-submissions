class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        l=len(nums)
        if len(nums)==1:
            return nums[0]
        for i  in nums:
            if i in dic:
                dic[i]+=1
                if dic[i]>(l/2):
                    return i
            else:
                dic[i]=1
        