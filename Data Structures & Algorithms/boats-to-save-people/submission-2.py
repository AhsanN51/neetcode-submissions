class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=sorted(people)
        l=0
        r=len(n)-1
        b=0
        while (l<=r):
           # print(l,r,"\t",n[l],n[r])
            s=n[l]+n[r]
            if s<=limit:
                b+=1
                l+=1
                r-=1
            elif n[r]<=limit:
                b+=1
                r-=1
            elif l==r:
                b+=1
                l+=1
            else:
                r-=1
           # print("ed ",l,r,"\t",n[l],n[r],b)
        return b