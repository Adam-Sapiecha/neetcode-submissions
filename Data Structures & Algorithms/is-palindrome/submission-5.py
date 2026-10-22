class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        s = "".join(c for c in s if c.isalnum())
        s = s.lower()
        if len(s) < 2:
            return True
        x = 0
        y = len(s) - 1
        while x < y:
            if s[x] != s[y]:
                return False

            x += 1
            y -= 1

        return True




