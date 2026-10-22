class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lista = list(set(nums))
        lista.sort()
        lista2 = []
        k = 1
        max_len = 1
        print(lista)
        for i in range(len(lista) - 1):
            if lista[i] + 1 == lista[i+1]:
                k += 1
                lista2.append(k)
            else:
                k = 1
        
        if not lista2:
            max_len = 1
        else:
            max_len = max(lista2)
        return max_len