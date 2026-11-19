class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_num = 10**9

        while left <= right:
            mid = (left + right) // 2

            min_num = min(min_num, nums[mid])

            if nums[left] <= nums[mid]:
                if nums[right] < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if nums[left] >= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        
        return min_num
