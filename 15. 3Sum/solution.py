# 3Sum Solution

from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        output_map = defaultdict(list)

        for i in range(len(nums) - 1):
            seen = {}
            target = 0 - nums[i]
            for j in range(i+1, len(nums)):
                compliment = target - nums[j]
                if compliment in seen:
                    triplet = [nums[i],nums[j],compliment]
                    sorted_triplet = tuple(sorted(triplet))
                    output_map[sorted_triplet].append(triplet)
                    # output.append([nums[i],nums[j],compliment])
                seen[nums[j]] = j

        for key in output_map.keys():   
            output.append(key) 

        return output