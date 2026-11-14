class Solution:
    def countSubstrings(self, s: str) -> int:
        pal_count = 0
        n = len(s)

        def isPal(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return 0
            return 1

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    pal_count += 1
                else:
                    pal_count += isPal(i, j)
        
        return pal_count