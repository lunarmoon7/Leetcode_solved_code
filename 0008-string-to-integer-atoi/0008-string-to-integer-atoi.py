class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1
        
        for ch in s:
            if empty:
                if ch == ' ': continue
                elif ch == '-': sign = -1
                elif ch.isdigit(): n = int(ch)
                elif ch != '+': return 0
                empty = False
            else:
                if ch.isdigit():
                    n = n * 10 + int(ch)
                else: break
        if sign * n > MAX: return MAX
        elif sign * n < MIN: return MIN
        return sign * n
        