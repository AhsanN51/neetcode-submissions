class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        start=0
        stop=2
        dic_c=[["."]*len(board) for _ in range(len(board))]
        dic_g=[["."]*len(board) for _ in range(len(board))]
        g=[0,1,2]
        for i in range(len(board)):
            dic_r=[]
            if (i==3) | (i==6):
                g=[x+3 for x in g]
            for j in range(len(board[0])):
                #row
                if (board[i][j] in dic_r) & (board[i][j]!="."):
                    return False
                else:
                    dic_r.append(board[i][j])
                #column
                if (board[i][j] in dic_c[j]) & (board[i][j]!="."):
                    return False
                else:
                    dic_c[j][i]=board[i][j]
                #grid
                if (j>=6) & (board[i][j] !="."):
                    if (board[i][j] in dic_g[g[2]]):
                        return False
                    else:
                        dic_g[g[2]].append(board[i][j])
                elif (j>=3) & (board[i][j] !="."):
                    if (board[i][j] in dic_g[g[1]]):
                        return False
                    else:
                        dic_g[g[1]].append(board[i][j])
                elif (j>=0) & (board[i][j] !="."):
                    if  (board[i][j] in dic_g[g[0]]):
                        return False
                    else:
                        dic_g[g[0]].append(board[i][j])
        return True