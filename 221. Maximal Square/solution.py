class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def helper(row, col):
            if row >= rows or col >= cols:
                return 0
            
            if (row,col) not in cache:
                down = helper(row + 1, col)
                right = helper(row, col + 1)
                diag = helper(row + 1, col + 1)

                cache[(row,col)] = 0

                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diag) 
            
            return cache[(row,col)]
        
        helper(0,0)

        return max(cache.values()) ** 2