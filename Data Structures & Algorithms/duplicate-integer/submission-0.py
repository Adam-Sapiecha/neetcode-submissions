class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                print(j,i) 
                if nums[j] == nums[i] and  i != j:

                    a = True
              

        return a
