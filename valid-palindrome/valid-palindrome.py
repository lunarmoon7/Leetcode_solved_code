class Solution:
    def isPalindrome(self, s: str) -> bool:
        lists = [ch for ch in s.lower() if ch.isalnum() ]
        return lists == lists[::-1]