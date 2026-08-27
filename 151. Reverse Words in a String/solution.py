class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split()
        n = len(s_arr)

        if n == 1:
            return s.strip()

        i = 0
        j = n - 1

        while i < j:
            s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
            i += 1
            j -= 1
        
        return " ".join(s_arr)
     