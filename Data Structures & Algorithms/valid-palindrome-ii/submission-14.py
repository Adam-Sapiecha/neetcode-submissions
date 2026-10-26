class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pure_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        p2 = 0
        p1 = len(s) - 1
        
        while p2 < p1:
            if s[p2] != s[p1]:
                return is_pure_palindrome(p2 + 1, p1) or is_pure_palindrome(p2, p1 - 1)
            
            p2 += 1
            p1 -= 1
            
        return True
