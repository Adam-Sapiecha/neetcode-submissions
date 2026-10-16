class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = list(arr)
        for i in range(len(arr)):
            arr2[i] = -1
            for j in range(len(arr[i+1:len(arr)])):
                if arr[j+i+1] > arr2[i]:
                    arr2[i] = arr[i+1+j]
        arr2[len(arr2)-1] = -1
        return arr2
                    