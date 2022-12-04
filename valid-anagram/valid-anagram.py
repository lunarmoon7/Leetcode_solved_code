class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)
        
        ret1 = sc - tc
        ret2 = tc - sc
        return False if ret1 or ret2 else True