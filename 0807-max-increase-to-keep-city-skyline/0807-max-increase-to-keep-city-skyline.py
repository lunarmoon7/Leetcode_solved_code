class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(row[i] for row in grid) for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
        return ans