class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = [[1]]

        for i in range(1, numRows):
            arr = [1] * (i + 1)
            for j in range(i+1):
                if j != 0 and j != i:
                    arr[j] = dp[i-1][j-1] + dp[i-1][j]

            dp.append(arr)

        return dp
                    