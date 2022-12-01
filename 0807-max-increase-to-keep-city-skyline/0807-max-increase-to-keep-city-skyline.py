class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        cnt = 0
        row, col = len(grid), len(grid[0])
        upDown, leftRight = [], []
        for x in range(row):
            leftRight.append(max(grid[x]))
            
        
        for y in range(col):
            maxs = 0
            for x in range(row):
                maxs = max(maxs, grid[x][y])
            upDown.append(maxs)
    
        for x in range(row):
            w = leftRight[x]
            for y in range(col):
                h = upDown[y]
                cnt += min(w, h) - grid[x][y]        
        return cnt
    
    
                