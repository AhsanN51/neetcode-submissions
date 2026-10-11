class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for n in nums:
            
            dic[n]=1+dic.get(n,0)

            if len(dic)<=2:
                continue
            
            dic2={}
            for k,v in dic.items():
                if v>1:
                    dic2[k]=v-1
            dic=dic2
        #print(dic,len(nums))
        return [c for c in dic if nums.count(c)>(len(nums)//3)]