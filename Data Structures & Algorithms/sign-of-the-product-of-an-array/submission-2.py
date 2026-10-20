class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        for i in nums:
            if i == 0:
                return 0
            y = abs(i)
            x = x * (i/y)
        return int(x)