class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            else:
                i = i - j + 1
                j = 0
        
        return -1

    