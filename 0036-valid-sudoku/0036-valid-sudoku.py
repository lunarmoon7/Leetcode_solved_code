class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        
        rows = [[0] * n for _ in range(n)]
        cols = [[0] * n for _ in range(n)]
        subs = [[0] * n for _ in range(n)]
        
        for x in range(n):
            for y in range(n):
                
                if board[x][y] == ".": continue
                
                pos = int(board[x][y]) - 1
                
                if rows[x][pos] == 1:
                    return False
                rows[x][pos] = 1
                
                if cols[y][pos] == 1:
                    return False
                cols[y][pos] = 1
                
                idx = (x // 3) * 3 + y // 3
                if subs[idx][pos] == 1:
                    return False
                subs[idx][pos] = 1
                
        return True
                    