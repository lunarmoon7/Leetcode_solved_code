class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        op = False
        if s[0] == "-":
            op = True
            s = s.replace("-", "")
        s = ''.join(reversed(s))
        if op:
            s = "-" + s
        x = int(s)
        return x if -2**31 < x < 2**31 - 1  else 0
        