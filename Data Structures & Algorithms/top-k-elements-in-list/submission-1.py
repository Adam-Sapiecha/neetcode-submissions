class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            klucz = i
            if i not in dic:
                dic[klucz] = 0
            dic[klucz] += 1
        wynik = sorted(dic, key = lambda x: dic[x], reverse = True)
        return wynik[:k]
