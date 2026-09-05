class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]

        for row in triangle[1:]:
            current = []

            for i, value in enumerate(row):
                if i == 0:
                    current.append(dp[0] + value)
                elif i == len(row) - 1:
                    current.append(dp[-1] + value)
                else:
                    current.append(value + min(dp[i], dp[i-1]))
            
            dp = current
        
        return min(dp)