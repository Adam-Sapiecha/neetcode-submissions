class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + '#' + strs[i]
        napis = ''.join(strs)
        print(napis)
        return napis
    def decode(self, s: str) -> List[str]:
        lista = list(s)
        lista2 = []
        i = 0

        while i < len(lista):
            j = i

            while lista[j] != "#":
                j += 1

            dlugosc = int(s[i:j])

            x = ''
            for k in range(j + 1, j + 1 + dlugosc):
                x += lista[k]

            lista2.append(x)
            i = j + 1 + dlugosc

        return lista2