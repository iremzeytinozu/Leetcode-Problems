class Solution(object):
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        columns = len(matrix[0])

        low = 0
        high = rows * columns - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = matrix[mid // columns][mid % columns]

            if target < mid_value:
                high = mid -1
            elif target > mid_value:
                low = mid + 1
            else:
                return True

        return False 