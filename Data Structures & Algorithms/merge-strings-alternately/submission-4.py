class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        w1=word1
        w2=word2
        r=""
        while i<len(w1) and i<len(w2):
            r+=w1[i]+w2[i]
            i+=1
            print(r)
        l=w2[i:] if len(w1)==i else w1[i:]
        r+="".join(l)
        #print("final:",r)
        return r