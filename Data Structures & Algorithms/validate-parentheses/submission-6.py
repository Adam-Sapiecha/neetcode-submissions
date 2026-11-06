class Solution:
    def isValid(self, s: str) -> bool:
        stos = []
        prawe = [')',']','}']
        lewe = ['(', '[', '{']
        for i in s:
            if stos is None or i in lewe:
                stos.append(i)
            else:
                if len(stos) > 0 and prawe.index(i) == lewe.index(stos[-1]):
                    stos.pop()
                else:
                    return False
            
        if len(stos) == 0:
            return True
        else:
            return False