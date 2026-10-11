class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sarr=[[0]*len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            self.sarr[r][0]=matrix[r][0]
            for c in range(1,len(matrix[0])):
                self.sarr[r][c]=self.sarr[r][c-1]+matrix[r][c]
       # print(self.sarr)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        for r in range(row1,row2+1):
            if col1==0:
                sum+=self.sarr[r][col2]
            else:
                sum+=self.sarr[r][col2]-self.sarr[r][col1-1]
        return sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)