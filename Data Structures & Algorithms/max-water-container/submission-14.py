class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lewy = 0
        prawy = len(heights) - 1
        maks = 0
        g = 1
        while lewy < prawy :
            dlugosc = len(heights)
            odleglosc = prawy - lewy
            pole = odleglosc * min(heights[lewy], heights[prawy])
            maks = max(maks, pole)
            mniejszy = min(heights[lewy], heights[prawy])
            if mniejszy == heights[prawy]:
                prawy -=1
            elif mniejszy == heights[lewy]:
                lewy +=1
        return(maks)