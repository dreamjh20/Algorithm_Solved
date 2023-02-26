# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = max(nums)
        
        for index, value in enumerate(nums):
            if peak == value:
                return index
