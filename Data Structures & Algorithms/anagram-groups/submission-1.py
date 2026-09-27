class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            st="".join(sorted(s))
            if st in dic:
                dic[st].append(s)
            else:
                dic[st]=[s]
        return [val for val in dic.values()] 