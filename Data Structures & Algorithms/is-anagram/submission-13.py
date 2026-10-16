class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        licznik = {}
        licznik2 = {}
        for znak in s:
            if znak in licznik:
                licznik[znak] += 1
            else:
                licznik[znak] = 1
        for znak in t:
            if znak in licznik2:
                licznik2[znak] += 1
            else:
                licznik2[znak] = 1
        if licznik == licznik2:
            return True
        else:
            return False