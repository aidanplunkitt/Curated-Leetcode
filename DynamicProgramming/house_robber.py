# https://leetcode.com/problems/house-robber/
# O(n) time, O(1) space

class Solution:
    def rob(self, nums: List[int]) -> int:
        highest = neighbor = 0
        for val in nums:
            neighbor, highest = highest, max(neighbor + val, highest)
        return highest