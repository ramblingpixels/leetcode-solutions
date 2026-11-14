class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            curr_len = right - left + 1

            max_len = max(max_len, curr_len)
        
        return max_len