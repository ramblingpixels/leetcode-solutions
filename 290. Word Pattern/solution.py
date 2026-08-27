class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        m = len(s)
        
        mapping = {}
        i = 0
        j = 0
        words = s.split()

        if n != len(words):
            return False

        while i < n and j < m:
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[j]:
                    return False
            else:
                if words[j] in mapping.values():
                    return False
                mapping[pattern[i]] = words[j]

            i += 1
            j += 1
        
        return True
            
            
