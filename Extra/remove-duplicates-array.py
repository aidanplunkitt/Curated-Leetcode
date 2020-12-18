# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# O(n) time, O(1) space

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        del nums[i+1:]
        return i+1