class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        used = False

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]
        n1 = len(nums1)
        n2 = len(nums2)

        arr1 = [0]*(n+1)
        arr2 = [0]*(n+1)
        arr1[1] = nums1[0]
        arr2[1] = nums2[0]

        for i in range(2, n1+1):
            arr1[i] = max((arr1[i-2] + nums1[i-1]), arr1[i-1])
        
        for i in range(2, n2+1):
            arr2[i] = max((arr2[i-2] + nums2[i-1]), arr2[i-1])

        return max(arr1[n1], arr2[n2])
        
        