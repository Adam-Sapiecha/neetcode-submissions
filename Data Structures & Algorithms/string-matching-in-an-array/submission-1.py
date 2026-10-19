from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = []
        for i, word in enumerate(words):
            for j in range(i + 1, len(words)):
                if word in words[j]:
                    result.append(word)
                    break   
        return result
