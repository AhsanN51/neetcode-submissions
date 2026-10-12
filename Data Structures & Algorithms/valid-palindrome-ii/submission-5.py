class Solution:
    def validPalindrome(self, s: str) -> bool:
        """def ispal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        """
        
        
        
        l=0
        r=len(s)-1
        #flag=False


        while(l<=r):
           # print("st: ",s[l],s[r],l,r)
            if s[l] != s[r] :
                sl=s[l+1:r+1]
                sr=s[l:r]
                return sl==sl[::-1] or sr==sr[::-1]
            print("ed:",s[l],s[r],l,r)    
            l+=1
            r-=1
        return True