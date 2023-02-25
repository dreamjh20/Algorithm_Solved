# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sum 함수로 list 덧셈해 2D Matrix를 List로 변환
        if target in sum(matrix, []):
            return True
        
        return False
