class Solution:
    def isValid(self, s: str) -> bool:
        stos = []
        pasuje = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in pasuje.values():
                stos.append(i)
            else:
                if len(stos) > 0 and pasuje[i] == stos[-1]:
                    stos.pop()
                else:
                    return False
            
        return len(stos) == 0
