class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                smaller_index = stack.pop()
                result[smaller_index] = nums[i]
            stack.append(i)
        
        m = len(stack)

        if m > 1:
            for i in range(1, m):
                if nums[stack[i]] < nums[stack[i-1]]:
                    result[stack[i]] = nums[stack[i-1]]

        return result
