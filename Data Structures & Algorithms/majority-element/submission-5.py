class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
       
        c=nums[0]
        v=1
        for i in range(1,len(nums)):
            #print("s",i)
            if v==0:
                # print("c")
                c=nums[i]
            if c==nums[i]:
                v+=1
               # print("w")
            else:
                v-=1
                #print("l")
            
               
           # print(c,v)
        return c