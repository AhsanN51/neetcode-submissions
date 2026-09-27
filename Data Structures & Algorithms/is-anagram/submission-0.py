class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for st in s:
            if st in d1:
                d1[st]+=1
            else:
                d1[st]=1
        for st in t:
            if st in d2:
                d2[st]+=1
            else:
                d2[st]=1
        if d1 == d2:
            return True
        else:
            return False