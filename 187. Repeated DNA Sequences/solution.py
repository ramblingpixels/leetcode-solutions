class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        seen = set()
        result = set()

        for i in range(n-9):
            subs = s[i: i+10]

            if subs in seen:
                result.add(subs)
            else:
                seen.add(subs)
        
        return list(result)