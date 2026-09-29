class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs=[set() for _ in range(9)]
        cs=[set() for _ in range(9)]
        gs=[set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                val=board[r][c]
                if val==".":
                    continue
                g=(r//3)*3+(c//3)
                if (val in rs[r]) or (val in cs[c]) or (val in gs[g]):
                    return False
                rs[r].add(val)
                cs[c].add(val)
                gs[g].add(val)
        return True
                    