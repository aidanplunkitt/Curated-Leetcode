# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
# O(n) time, O(len(charset)) space

import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_count, last_unique = 0, -1
        for i, c in enumerate(s):
            if c in seen:
                last_unique = max(last_unique, seen[c])
            seen[c] = i
            max_count = max(max_count, i - last_unique)
            
        return max_count