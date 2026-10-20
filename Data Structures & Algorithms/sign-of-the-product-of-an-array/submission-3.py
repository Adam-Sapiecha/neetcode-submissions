class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        for i in nums:
            if i == 0:
                return 0
            x = x * i
        return int(x/abs(x))