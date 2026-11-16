class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
         
        n = len(nums)
        count = 0
        p = 1
        left = 0

        for right in range(n):
            
            p = p*nums[right]

            while p >= k:
                p = p // nums[left]
                left += 1
            
            count += right - left + 1
        
        return count
