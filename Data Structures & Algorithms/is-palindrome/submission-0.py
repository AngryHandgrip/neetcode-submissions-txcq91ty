class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not self.alphanumeric(s[i]):
                i += 1
                continue
            if not self.alphanumeric(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    
    def alphanumeric(self, s: str) -> bool:
        return (ord('a') <= ord(s) <= ord('z') or
                ord('A') <= ord(s) <= ord('Z') or
                ord('0') <= ord(s) <= ord('9'))
            