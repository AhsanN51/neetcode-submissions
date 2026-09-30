class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for st in s:
            if len(l)==0:
                l.append(st)
                continue
            if st==')' and l[-1]=='(':
                l.pop()
            elif st=='}' and l[-1]=='{':
                l.pop()
            elif st==']' and l[-1]=='[':
                l.pop()
            else:
                l.append(st)
        return (len(l)==0)