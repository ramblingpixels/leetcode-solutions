class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right])*(right - left)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            max_area = max(max_area, area)
        
        return max_area
                


