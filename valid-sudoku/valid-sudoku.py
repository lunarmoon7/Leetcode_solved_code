class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = col = 9
        
        def checkRowCol(x, y):
            # Check Row
            num = board[x][y]
            for i in range(9):
                if i == y: continue
                if board[x][i] == num:
                    return False
            # Check Col
            for i in range(9):
                if i == x: continue
                if board[i][y] == num:
                    return False
            return True
                
        # Check 3*3 sub boxes
        def checkSub(x, y):
            q = x // 3
            r = y // 3
            check = [False] * 10
            for i in range(q * 3, q * 3 + 3):
                for j in range(r * 3, r * 3 + 3):
                    if board[i][j] == '.': continue
                    num = int(board[i][j])
                    if check[num]:
                        return False
                    check[num] = True
            return True
        
        for x in range(row):
            for y in range(col):
                if board[x][y] == '.': continue
                if not checkRowCol(x, y) or not checkSub(x, y):
                    return False
        return True