class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = set(nums)
        nums[:] = sorted(nums2)
        return len(nums)