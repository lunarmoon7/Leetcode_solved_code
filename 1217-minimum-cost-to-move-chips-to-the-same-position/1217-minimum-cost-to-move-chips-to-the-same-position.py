class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cost = 0
        even_cnt, odd_cnt = 0, 0
        
        for num in position:
            if num % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)