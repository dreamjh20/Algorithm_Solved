# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        # 가장 최근에 탐색된 값이 0인 index
        lastZero = 0;
        for index, value in enumerate(nums):
            if nums[index] != zero:
                nums[index], nums[lastZero] = nums[lastZero], nums[index]
                lastZero += 1