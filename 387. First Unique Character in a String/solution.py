class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        n = len(s)

        for char in s:
            count[char] = count.get(char, 0) + 1
        
        first_unique_char = None

        for char, freq in count.items():
            if freq == 1:
                first_unique_char = char
                break
        
        for i in range(n):
            if s[i] == first_unique_char:
                return i

        return -1