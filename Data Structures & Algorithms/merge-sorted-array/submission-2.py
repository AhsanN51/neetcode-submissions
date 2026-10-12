class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=m+n-1
        m-=1
        n-=1
        for i in range(l,-1,-1):
            #print("st :",m,n,nums1)
            if n==-1:
                nums1[i]=nums1[m]
                m-=1
                continue
            if m==-1:
                nums1[i]=nums2[n]
                n-=1
                continue
            if nums1[m]>nums2[n]:
                nums1[i]=nums1[m]
                nums1[m]=0
                m-=1
            else:
                nums1[i]=nums2[n]
                n-=1
            #print("end: ",m,n,nums1)
                  