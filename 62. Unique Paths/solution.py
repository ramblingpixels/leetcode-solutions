class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m+1):
            arr[i][1] = 1
        
        for i in range(1, n+1):
            arr[1][i] = 1

        for i in range(2, m+1):
            for j in range(2, n+1):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
        
        return arr[m][n]