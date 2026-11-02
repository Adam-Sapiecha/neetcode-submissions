class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lewy = 0
        prawy = len(heights) - 1
        maks = 0
        dlugosc = len(heights)
        while lewy < prawy:
            h_lewy = heights[lewy]
            h_prawy = heights[prawy]
            odleglosc = prawy - lewy
            if h_lewy > h_prawy:
                mniejszy = h_prawy
            else:
                mniejszy = h_lewy
            pole = odleglosc * mniejszy
            if pole > maks:
                maks = pole
            if mniejszy == h_prawy:
                prawy -=1
            else:
                lewy +=1
        return(maks)