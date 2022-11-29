class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        l = list(str(num))
        
        for i in range(len(l)):
            if l[i] == "6":
                l[i] = "9"
                break
        return ''.join(l)
        
            