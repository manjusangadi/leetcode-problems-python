class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ''.join(ch.lower() for ch in s if ch.isalnum())
        return ch == ch[::-1]
        
