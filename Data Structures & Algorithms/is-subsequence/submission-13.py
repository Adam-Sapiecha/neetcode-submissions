class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in s:
            j = t.find(i, start)
            if j == -1:
                return False
            start = j + 1
        return True
