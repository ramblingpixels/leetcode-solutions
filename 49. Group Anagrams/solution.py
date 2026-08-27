class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        result = []

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(str)
            else:
                anagram_map[sorted_str] = [str]
        
        for value in anagram_map.values():
            result.append(value)

        return result

        