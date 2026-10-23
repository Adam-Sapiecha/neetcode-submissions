from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = 0
        y = len(numbers) - 1

        while x < y:
            aktualna_suma = numbers[x] + numbers[y]

            if aktualna_suma == target:
                return [x + 1, y + 1]

            elif aktualna_suma < target:
                x += 1

            else:
                y -= 1
