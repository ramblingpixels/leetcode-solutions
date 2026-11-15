from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        abc_count = defaultdict(int)
        count = 0

        for right in range(n):
            char_right = s[right]
            abc_count[char_right] += 1

            while len(abc_count) == 3:
                count += n - right

                char_left = s[left]
                abc_count[char_left] -= 1
                if abc_count[char_left] == 0:
                    del abc_count[char_left]
                left += 1
            
        return count
            
            
            
