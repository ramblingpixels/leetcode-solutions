class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return n
        
        current_max = 1
        curr_str = s[0]

        for i in range(1,n):
            if s[i] not in curr_str:
                curr_str = curr_str + s[i]
            else:
                index = curr_str.find(s[i])
                result = curr_str[index + 1:]
                curr_str = result + s[i]
            
            current_max = max(current_max, len(curr_str))
    
        
        return current_max       


        