class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        r=[0]*len(t)
        st=[]
        for i in range(len(t)-1,-1,-1):
            #print(st,r)
            while st and st[-1][0]<=t[i]:
                temp,j=st.pop()
                #r[j]=i-j
            if st:
                r[i]=st[-1][1]-i
            st.append([t[i],i])
        return r