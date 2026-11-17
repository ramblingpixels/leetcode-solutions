class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)

        # Step 1: Find the first decreasing position from right
        i = length - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # No greater permutation exists
        if i < 0:
            return -1

        # Step 2: Find the smallest digit greater than nums[i]
        j = length - 1

        while nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap the two digits
        nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse everything after i
        nums[i + 1:] = reversed(nums[i + 1:])

        # Step 5: Check 32-bit signed integer limit
        result = int(''.join(nums))

        return result if result <= 2**31 - 1 else -1