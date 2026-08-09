# 64 Solution

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        arr = [[0] * (n+1) for _ in range(m+1)]

        arr[1][1] = grid[0][0]

        for i in range(2, m+1):
            arr[i][1] = arr[i-1][1] + grid[i-1][0]

        for i in range(2, n+1):
            arr[1][i] = arr[1][i-1] + grid[0][i-1]

        for i in range(2, m+1):
            for j in range(2, n+1):
                arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + grid[i-1][j-1]

        return arr[m][n]



        