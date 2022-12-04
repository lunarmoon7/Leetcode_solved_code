class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        subs = [set() for _ in range(n)]
        
        for x in range(n):
            for y in range(n):
                val = board[x][y]
                if val == ".": continue
                
                if val in rows[x]: 
                    return False
                rows[x].add(val)
                
                if val in cols[y]: 
                    return False
                cols[y].add(val)                
                
                idx = (x // 3) * 3 + y // 3
                if val in subs[idx]: 
                    return False
                subs[idx].add(val)
                
        return True
                    