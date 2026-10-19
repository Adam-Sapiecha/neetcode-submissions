class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        kandydat = None
        glosy = 0

        for num in nums:
            if glosy == 0:
                kandydat = num

            if num == kandydat:
                glosy += 1
            else:
                glosy -= 1

        return kandydat
