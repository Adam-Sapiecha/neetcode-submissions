class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        x = 0
        for i in nums:
            if i == 1:
                x += 1
            elif i == 0:
                if x > a:
                    a = x
                x = 0
        if x > a:
            a = x
        return a
                            