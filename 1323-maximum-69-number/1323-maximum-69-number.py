class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        n = len(s)
        for i in range(n):
            if s[i] == "6":
                s = s[:i] + "9" + s[i+1:]
                break
        return s
        
            