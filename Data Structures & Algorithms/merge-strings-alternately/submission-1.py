class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=0
        w2=0
        wd1=list(word1)
        wd2=list(word2)
        flag=True
        minl=min(len(wd1),len(wd2))
        #print(minl)
        r=""
        """
        while w1 <minl and w2<minl: 
            if flag==True:
                flag=False
                r+=wd1[w1]
                w1+=1
                
                    break
            else:
                flag=True
                r+=wd2[w2]
                w2+=1
                
                    break
            print(r,w1,w2)

        """
        i=0
        while i<minl:
            if flag==True:
                flag=False
                r+=wd1[w1]
                w1+=1
            else:
                flag=True
                r+=wd2[w2]
                w2+=1
                i+=1
        
        if len(wd1)==minl:
            #print("w1")
            r+="".join(wd2[(minl):])
        else:
            #print("w2")
            r+="".join(wd1[(minl):])
       # print(r)
        return r