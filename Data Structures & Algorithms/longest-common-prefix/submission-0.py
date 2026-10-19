class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        
        x = 0
        a = ""
        first_word = strs[0] # Zapamiętujemy CAŁE pierwsze słowo, a nie tylko jedną literę
        
        while x < len(first_word): # Używamy < zamiast !=, co jest bezpieczniejsze
            for string in strs:
                # 1. Zabezpieczenie przed za krótkim słowem
                # 2. Porównanie litery aktualnego słowa z literą PIERWSZEGO słowa
                if x >= len(string) or string[x] != first_word[x]:
                    return a
            
            a += first_word[x] # Bezpiecznie dodajemy literę, którą właśnie zweryfikowaliśmy we wszystkich słowach
            x += 1
            
        return a
