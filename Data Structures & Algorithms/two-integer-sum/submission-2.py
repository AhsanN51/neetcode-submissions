class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for n in range(len(nums)):
            dif=target -nums[n]
            if dif in dic:
                return [dic[dif],n]
            else:
                dic[nums[n]]=n
