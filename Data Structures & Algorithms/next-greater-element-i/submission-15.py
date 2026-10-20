class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lista = []
        for i in range(len(nums1)):
            if nums2.index(nums1[i])+1 >= len(nums2):
                lista.append(-1)
            elif nums1[i] >= nums2[nums2.index(nums1[i])+1]:
                for j in range(nums2.index(nums1[i])+1, len(nums2)):
                    if nums1[i] < nums2[j]:
                        lista.append(nums2[j])
                    elif nums1[i] >= nums2[j]:
                        if j == len(nums2)-1:
                            lista.append(-1)
                        else:    
                            pass
            else:
                lista.append(nums2[nums2.index(nums1[i])+1])
        return lista
            