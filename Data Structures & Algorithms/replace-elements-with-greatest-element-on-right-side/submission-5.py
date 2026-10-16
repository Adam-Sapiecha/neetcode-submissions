from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maks_po_prawej = -1

        for i in range(len(arr) - 1, -1, -1):
            

            stara_wartosc = arr[i]
            

            arr[i] = maks_po_prawej
            
 
            if stara_wartosc > maks_po_prawej:
                maks_po_prawej = stara_wartosc
                
        return arr
