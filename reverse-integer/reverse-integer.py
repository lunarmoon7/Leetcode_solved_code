class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        op = False
        if s[0] == "-":
            op = True
            s = s.replace("-", "")
        s = ''.join(reversed(s))
        x = int(s)
        if op:
            x = -x
        
        return x if -2**31 < x < 2**31 - 1  else 0
        