class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=operations
        r=[]
        for o in ops:
            
            if o =='+':
                a,b=r.pop(),r.pop()
                r.append(b)
                r.append(a)
                r.append(int(a)+int(b))
            elif o=='C':
                r.pop()
            elif o=='D':
                b=int(r.pop())
                a=2*b
                r.append(b)
                r.append(a)
            else:
                r.append(o)
            #print(r,o)
        s=0
        for x in r:
            s+=int(x)
        return s
            