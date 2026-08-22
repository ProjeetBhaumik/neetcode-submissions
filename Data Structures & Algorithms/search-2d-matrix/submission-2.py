class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        
        l = 0
        r = (rows * cols) - 1
        while l <= r:
            m = l + (r-l) // 2
            row, column = m // cols, m % cols
            if target > matrix[row][column]:
                l = m + 1
            elif target < matrix[row][column]:
                r = m - 1
            else:
                return True
        return False