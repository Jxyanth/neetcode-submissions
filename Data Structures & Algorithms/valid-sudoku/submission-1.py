class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val=='.':
                    continue
                row_key = (val,"row",i)
                col_key = (val,"col",j)
                box_key = (val,"box",i//3,j//3)
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                else:
                    seen.add((val,"row",i))
                    seen.add((val,"col",j))
                    seen.add((val,"box",i//3,j//3))
        return True
