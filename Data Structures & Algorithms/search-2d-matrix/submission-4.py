class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        mt=matrix
        top=0
        down=r-1
        m=0
        #print("row")
        while top<=down:
            m=(top+down)//2    
           # print("st: ",mt[top][0],mt[down][0],mt[m][0])
            if target > matrix[m][-1]:
                top = m+1
            elif target < matrix[m][0]:
                down = m -1
            else:
                break
            #print("ed: ",mt[top][0],mt[down][0],mt[m][0])
        else:
            return False        
        left=0
        right=c-1
        m=(top+down)//2
        #print("col")
       # print(m)
        while left<=right:
            mid=(left+right)//2    
            #print("st: ",mt[m][left],mt[m][right],mt[m][mid])
            if matrix[m][mid]==target:
                return True
            elif matrix[m][mid]<target:
                left=mid+1
            else:
                right=mid-1
            #print("ed: ",mt[m][left],mt[m][right],mt[m][mid])
        else:
            return False    