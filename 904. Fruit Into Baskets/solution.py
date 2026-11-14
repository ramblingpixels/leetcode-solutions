from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        fruit_map = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(n):
            fruit_map[fruits[right]] += 1

            if len(fruit_map) > 2:
                while len(fruit_map) > 2:
                    if fruit_map[fruits[left]] == 1:
                        del fruit_map[fruits[left]]
                    else:
                        fruit_map[fruits[left]] -= 1
                    left += 1 
            
            curr_len = right - left + 1

            max_len = max(max_len, curr_len)
        
        return max_len