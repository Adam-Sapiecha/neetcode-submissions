class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        print(s)
        lista = []
        for i in range(len(s)):
            wskaznik = i
            lewy = i + 1
            prawy = len(s)-1
            while lewy < prawy:
                trojka = [s[wskaznik], s[lewy], s[prawy]]
                if sum(trojka) == 0:
                    if trojka not in lista:
                        lista.append(trojka)
                    lewy += 1
                else:
                    if sum(trojka) > 0:
                        prawy -= 1
                        continue
                    elif sum(trojka) < 0:
                        lewy += 1
                        continue

        return lista
