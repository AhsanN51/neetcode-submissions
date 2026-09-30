class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        dic={')':'(',']': '[', '}': '{'}
        for st in s:
            if st in dic:
                if not l or l.pop() != dic[st]:
                    return False
            else:
                l.append(st)
        return not l