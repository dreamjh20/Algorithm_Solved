# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        listSum = sum(nums)

        for index, value in enumerate(nums):
            # index 왼쪽 합과 오른쪽 합 (전체 합 - 왼쪽 합 - index 값) 비교
            if leftSum == (listSum - leftSum - value):
                return index
            leftSum = leftSum + value

        # pivot index 존재하지 않으면 -1 반환
        return -1
