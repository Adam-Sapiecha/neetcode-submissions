class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ''
        k = 0
        
        for i in range(min([len(word1), len(word2)])):
            string += word1[i] + word2[i]
            k = i
        if len(word1) > len(word2):    
            string += word1[k+1:len(word1)]
        elif len(word1) < len(word2):     
            string += word2[k+1:len(word2)]
        else:
            pass
        return string 