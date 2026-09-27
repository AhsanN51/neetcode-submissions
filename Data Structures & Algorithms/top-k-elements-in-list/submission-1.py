class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        sdic=sorted(dic.keys(),key=lambda key:dic[key],reverse=True)
        return [sdic[n] for n in range(k)]
        