class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupy = {}
        for slowo in strs:
            klucz = "".join(sorted(slowo))
            if klucz not in grupy:
                grupy[klucz] = []
            grupy[klucz].append(slowo)
        return list(grupy.values())