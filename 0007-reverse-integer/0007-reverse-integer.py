class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        op = False
        
        if x < 0: op = True
        
        s = ''.join(reversed(s.replace("-", "")))
        x = int(s)
        
        if op:
            x = -x
        
        return x if -2**31 < x < 2**31 - 1  else 0
        