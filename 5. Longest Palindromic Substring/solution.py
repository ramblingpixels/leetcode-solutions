class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        longest_pal = ""

        def expand(left, right):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]


        for i in range(len(s)):
            odd_pal = expand(i, i)
            even_pal = expand(i-1, i)

            longest_pal = max(longest_pal, odd_pal, even_pal, key = len)
        
        return longest_pal
        