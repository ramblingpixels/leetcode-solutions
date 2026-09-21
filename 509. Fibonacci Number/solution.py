class Solution:
    def fib(self, n: int) -> int:
        dp = [0]* (n+1)
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        first, second = 1, 2

        for i in range(3, n):
            first, second = second, first + second
        

        return second