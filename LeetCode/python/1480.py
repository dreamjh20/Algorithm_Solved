# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(1,len(nums)):
            nums[index] += nums[index-1]

        return nums
