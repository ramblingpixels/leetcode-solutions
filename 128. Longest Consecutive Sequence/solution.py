class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        max_count = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                count = 1
                temp = num
                while (temp + 1) in nums_set:
                    count += 1
                    temp += 1
                max_count = max(count, max_count)

        return max_count