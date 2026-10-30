class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        lista = set()
        for i in range(len(s)):
            wskaznik = i
            lewy = i + 1
            prawy = len(s) - 1
            if s[i] > 0:
                break
            while lewy < prawy:
                trojka = (s[wskaznik], s[lewy], s[prawy])
                suma = s[wskaznik] + s[lewy] + s[prawy]
                if suma == 0:
                    lista.add(trojka)
                    while lewy < prawy and s[lewy] == s[lewy + 1]:
                        lewy += 1
                    while lewy < prawy and s[prawy] == s[prawy - 1]:
                        prawy -= 1
                    lewy += 1
                    prawy -= 1
                else:
                    if suma > 0:
                        prawy -= 1
                    elif suma < 0:
                        lewy += 1
        return [list(i) for i in lista]
