class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lewy = 0
        prawy = len(heights) - 1
        maks = 0
        dlugosc = len(heights)
        while lewy < prawy:
            odleglosc = prawy - lewy
            mniejszy = min(heights[lewy], heights[prawy])
            pole = odleglosc * mniejszy
            maks = max(maks, pole)
            if mniejszy == heights[prawy]:
                prawy -=1
            elif mniejszy == heights[lewy]:
                lewy +=1
        return(maks)