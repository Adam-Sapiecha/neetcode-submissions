class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        wynik = []
        dlugosc = len(nums)
        for i in range(len(nums)):
            suma = 1
            for j in range(len(nums)):
                if i == j:
                    pass
                else:
                    suma *= nums[j]
            wynik.append(suma)
        return wynik
