from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        s1_count = Counter(s1)

        for i in range(len(s2) - n + 1):
            window = s2[i:i+n]

            if Counter(window) == s1_count:
                return True
        
        return False
