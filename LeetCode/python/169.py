# 169. Majority Element
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keySet = set(nums)
        
        for key in keySet:
            if nums.count(key) > len(nums) / 2:
                return key