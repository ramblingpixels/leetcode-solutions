class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        count = {}
        result = 0
        hasOdd = False

        for char in s:
            count[char] = count.get(char, 0) + 1

        biggest_odd = 0

        for value in count.values():
            if value % 2 == 0:
                result += value
            else:
                result = result + value - 1
                hasOdd = True
                
        if hasOdd:
            result = result + 1

        return result
