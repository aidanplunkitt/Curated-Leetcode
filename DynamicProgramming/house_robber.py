# https://leetcode.com/problems/house-robber/
# O(n) time, O(n) space

class Solution:
    def rob(self, nums: List[int]) -> int:
        max_val = [0, 0, 0] + [0] * len(nums)
        i = 3
        while i < len(max_val):
            max_val[i] = nums[i-3] + max(max_val[i-2], max_val[i-3])
            i += 1
        return max(max_val)