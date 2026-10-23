class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return
        x = 0
        k = ''
        y = len(s) - 1
        while x <= y:
            if x == y:
                break
            k = s[x]
            s[x] = s[y]
            s[y] = k
            x+=1
            y-=1
