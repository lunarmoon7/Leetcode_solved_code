class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        
        return True if s == ''.join(reversed(s)) else False