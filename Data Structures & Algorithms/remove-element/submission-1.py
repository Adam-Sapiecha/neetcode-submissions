class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lista = []
        while len(nums) > 0 :
            if nums[-1] == val:
                nums.pop()
            elif nums[-1] != val:
                lista.append(nums[-1])
                nums.pop()
        k = len(lista)
        nums[:] = lista
        return k