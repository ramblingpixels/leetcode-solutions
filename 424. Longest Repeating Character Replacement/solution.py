class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    # Fixed-size array for 'a' through 'z'
    count = [0] * 26
    max_len = 0
    max_freq = 0
    left = 0

    for right in range(len(s)):
      # 1. Map character to index 0-25 and increment frequency
      idx = ord(s[right]) - ord('a')
      count[idx] += 1

      # 2. Track the highest frequency globally in the window
      max_freq = max(max_freq, count[idx])

      # 3. Check window validity
      current_window_length = right - left + 1
      if current_window_length - max_freq > k:
        # Shrink window from the left
        left_idx = ord(s[left]) - ord('a')
        count[left_idx] -= 1
        left += 1

      # 4. Update max length
      max_len = max(max_len, right - left + 1)

    return max_len