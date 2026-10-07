class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """p,s=position,speed
        t=[]
        st=[]
        r=0
        for i in range(len(p)):
            t=(target-p[i])/s[i]
            while st and p[i]<st[-1][0] and t<=st[-1][1]:
                st.pop()
            st.append(((p[i]),t))
            #t.append((p[i],(target-p[i])/s[i]))
            print(st)
        print("len:",len(st))
        #r=0
        """

        pr=[(p,s) for p,s in zip(position,speed)]
        pr.sort(reverse=True)
       # print(pr)
        st=[]
        for p,s in pr:
            st.append((target-p)/s)
            if len(st)>=2 and st[-1] <=st[-2]:
                st.pop()
        return len(st)




