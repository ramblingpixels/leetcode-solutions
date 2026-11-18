class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)

        i = length - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i == -1:
            return nums.reverse()
        
        j = length - 1

        while nums[j] <= nums[i]:
            j -= 1
        
        nums[j], nums[i] = nums[i], nums[j]

        nums[i+1:] = reversed(nums[i+1:])

        return nums
        