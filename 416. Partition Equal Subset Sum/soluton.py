def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    
    # If total is odd, can't split into two equal halves
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    # dp[i] = True if a subset summing to i is achievable
    dp = [False] * (target + 1)
    dp[0] = True  # sum 0 is always achievable (empty subset)
    
    for num in nums:
        # Traverse backwards to avoid reusing the same element twice
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    
    return dp[target]