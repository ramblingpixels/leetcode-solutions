from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        result = []

        if m > n:
            return []
        
        s1_count = Counter(p)

        for i in range(n-m+1):
            window = s[i:i+m]
            window_count = Counter(window)
            if window_count == s1_count:
                result.append(i)
        
        return result
    

      