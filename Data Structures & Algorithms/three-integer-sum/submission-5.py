class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        lista = set()
        for i in range(len(s)):
            wskaznik = i
            lewy = i + 1
            prawy = len(s)-1
            while lewy < prawy:
                trojka = (s[wskaznik], s[lewy], s[prawy])
                suma = sum(trojka)
                if suma == 0:
                    lista.add(trojka)
                    lewy += 1
                else:
                    if suma > 0:
                        prawy -= 1
                    elif suma < 0:
                        lewy += 1
            if s[i] > 0:
                return [list(i) for i in lista]
        return [list(i) for i in lista]