class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)

        result = [-1]*n

        for i in range(n):
            flag = 0
            for j in range(m):
                if not flag:
                    if nums2[j] == nums1[i]:
                        flag = 1
                else:
                    if nums2[j] > nums1[i]:
                        result[i] = nums2[j]
                        break
                    
        return result