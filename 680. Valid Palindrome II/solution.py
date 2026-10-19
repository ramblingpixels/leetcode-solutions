class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        n = len(s)
        right = n - 1

        def check_palindrome(left, right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True  

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (check_palindrome(left + 1, right) or check_palindrome(left, right - 1))

        return True

        
