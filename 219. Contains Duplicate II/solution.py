from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        duplicate_dict = defaultdict(int)

        for i in range(n):
            if nums[i] in duplicate_dict:
                if abs(i - duplicate_dict[nums[i]] <= k):
                    return True
            duplicate_dict[nums[i]] = i

        return False