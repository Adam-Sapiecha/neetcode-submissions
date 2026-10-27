class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val

        tekst = list(s)
        aktualne_przesuniecie = 0

        for i in range(n):
            aktualne_przesuniecie += diff[i]

            nowy_kod = ((ord(tekst[i]) - 97 + aktualne_przesuniecie) % 26) + 97
            tekst[i] = chr(nowy_kod)

        return "".join(tekst)

    #     zmiany = self.sumaShift(shifts, len(s))
    #     tekst = list(s)
    #     for m in range(len(s)):
    #         if zmiany[m] != 0:
    #             tekst[m] = chr(((ord(s[m]) - 97 + zmiany[m]) % 26) + 97)

    #     return ''.join(tekst)

    # def sumaShift(self, shifts, n):
    #     diff = [0] * (n + 1)
    #     for start, end, direction in shifts:
    #         val = 1 if direction == 1 else -1
    #         diff[start] += val
    #         diff[end + 1] -= val
    #     zmiany = [0] * n
    #     aktualne_przesuniecie = 0
    #     for i in range(n):
    #         aktualne_przesuniecie += diff[i]
    #         zmiany[i] = aktualne_przesuniecie

    #     return zmiany

    #     zmiany = self.sumaShift(shifts)
    #     tekst = list(s)
    #     for m, d in zmiany.items():
    #         tekst[m] = chr(((ord(s[m]) - 97 + d) % 26) + 97)
    #     print(tekst)
    #     return ''.join(tekst)

    # def sumaShift(self, shifts):
    #     dic = {}
    #     for i in shifts:
    #         for j in range(i[0], i[1] + 1):
    #             if i[2] == 1:
    #                 if j in dic:
    #                     dic[j] += 1
    #                 else:
    #                     dic[j] = 1

    #             if i[2] == 0:
    #                 if j in dic:
    #                     dic[j] -= 1
    #                 else:
    #                     dic[j] = -1
    #     return dic

    # k = list(s)
    # for y in shifts:
    #     for j in range(y[0],y[1]+1):
    #         if y[-1] == 1 and isinstance(k[j], int):
    #             if k[j] == 122:
    #                 k[j] = 97
    #             else:
    #                 k[j] = k[j] + 1
    #         elif y[-1] == 0 and isinstance(k[j], int):
    #             if k[j] == 97:
    #                 k[j] = 122
    #             else:
    #                 k[j] = k[j] - 1
    #         elif y[-1] == 1 and isinstance(k[j], str):
    #             if k[j] == 'z':
    #                 k[j] = 'a'
    #             else:
    #                 k[j] = ord(k[j]) + 1
    #         elif y[-1] == 0 and isinstance(k[j], str):
    #             if k[j] == 'a':
    #                 k[j] = 'z'
    #             else:
    #                 k[j] = ord(k[j]) - 1
    # for i in range(len(k)):
    #     if isinstance(k[i], int):
    #         k[i] = chr(k[i])
    #     else:
    #         pass
    # x = ''.join(k)
    # return x
    # def komasacjaSziftow(self, shifts):
