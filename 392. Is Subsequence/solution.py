class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i = 0
        j = 0
        
        if m == 0:
            return True


        for i in range(n):
            if t[i] == s[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                i += 1
        
        return False