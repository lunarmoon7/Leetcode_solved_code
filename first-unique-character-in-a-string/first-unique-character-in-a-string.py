class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        
        for idx, ch in enumerate(s):
            if c[ch] == 1:
                return idx
        return -1
            