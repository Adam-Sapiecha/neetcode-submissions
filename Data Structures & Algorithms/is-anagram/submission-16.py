class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}

        for num in s:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for num in t:
            if num in dic2:
                dic2[num] += 1
            else:
                dic2[num] = 1

        return dic == dic2