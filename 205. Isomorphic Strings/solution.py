class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mapping = {}
        t_mapping = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in s_mapping:
                if s_mapping[char_s] != char_t:
                    return False
            else:
                s_mapping[char_s] = char_t
            
            if char_t in t_mapping:
                if t_mapping[char_t] != char_s:
                    return False
            else:
                t_mapping[char_t] = char_s

        
        return True
