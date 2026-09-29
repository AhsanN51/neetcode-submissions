class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=list(s.lower())
        l=0
        r=len(s)-1
        while(l<r):
            if (s[l].isalnum()==False):
                l+=1
                continue
            elif (s[r].isalnum()==False):
                r-=1
                continue
            elif s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True