class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)         # m = rows 
        n = len(matrix[0])      # n = cols 
        L = 0                   # L = left 
        R = m * n -1            # R = right (total len - 1)

        while L <= R:
            mid = (L + R) // 2
            val = matrix[mid//n][mid%n]
            
            if (target < val):
                R = mid - 1
            elif (target > val):
                L = mid + 1
            else:
                return True

        return False 
