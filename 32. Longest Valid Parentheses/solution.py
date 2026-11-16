class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0

        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            
            if right > left:
                left = 0
                right = 0

            if left == right:
                max_len = max(max_len, 2*right)

        left = 0
        right = 0


        for char in reversed(s):
            if char == "(":
                left += 1
            else:
                right += 1
            
            if left > right:
                left = 0
                right = 0

            if left == right:
                max_len = max(max_len, 2*left)
        
        return max_len
        