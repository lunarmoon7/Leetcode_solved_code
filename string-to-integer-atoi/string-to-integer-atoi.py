class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) < 1: 
            return 0
        
        mins, maxs = -2**31, 2**31 - 1
        num = 0
        negative = False
        pos = 0
        
        if s[pos] == '-':
            negative = True
            pos += 1
        elif s[pos] == '+':
            pos += 1
            
        while pos < len(s):
            if not s[pos].isdigit():
                break
            
            num = num * 10 + int(s[pos])
            pos += 1
            
        num = -num if negative else num
        if num < mins:
            num = mins
        elif num > maxs:
            num = maxs
        return num