class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sClean = s.strip()
        index = sClean.rfind(' ')
        sCleanList = list(s.strip())
        return len(sCleanList[index+1:])
