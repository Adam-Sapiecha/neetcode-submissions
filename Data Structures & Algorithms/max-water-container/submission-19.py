class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lewy = 0
        prawy = len(heights) - 1
        maks = 0
        dlugosc = len(heights)
        while lewy < prawy:
            odleglosc = prawy - lewy
            if heights[lewy] > heights[prawy]:
                mniejszy = heights[prawy]
            else:
                mniejszy = heights[lewy]
            pole = odleglosc * mniejszy
            if pole > maks:
                maks = pole
            if mniejszy == heights[prawy]:
                prawy -=1
            else:
                lewy +=1
        return(maks)