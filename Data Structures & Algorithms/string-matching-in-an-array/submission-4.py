class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words:
            return []
        x = 0
        lista = []
        words.sort(key=len)
        while x < len(words):
            for i in range(x+1, len(words)):
                if words[x] in words[i]:
                    lista.append(words[x])  
                    break
            x += 1
        return lista