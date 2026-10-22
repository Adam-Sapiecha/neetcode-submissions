class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        maks = 0
        nums = set(nums)
        for i in nums:
            k = 1
            if i-1 not in nums:
                k = self.czyJest(nums, i)
            maks = max(maks, k)
        return maks

    def czyJest(self, nums, i):
        k = 1

        while i + 1 in nums:
            i += 1
            k += 1

        return k