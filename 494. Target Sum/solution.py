from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If target is out of reach, or (total+target) is odd, no valid subset exists
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        subset_sum = (total + target) // 2
        
        # Standard "count subsets with given sum" DP
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]
        
        return dp[subset_sum]