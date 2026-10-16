class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sClean = s.strip()
        index = sClean.rfind(' ')
        return len(sClean[index+1:])
