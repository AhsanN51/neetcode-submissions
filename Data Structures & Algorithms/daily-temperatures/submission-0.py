class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        r=[0]*len(t)
        st=[]
        for i in range(len(t)):
            while st and st[-1][0]<t[i]:
                temp,j=st.pop()
                r[j]=i-j
            st.append([t[i],i])
        return r