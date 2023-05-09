# 54. Spiral Matrix


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize the boundaries
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1
        
        result = []
        
        # Traverse the matrix in a spiral order
        while row_begin <= row_end and col_begin <= col_end:
            # Traverse the first row from left to right
            for i in range(col_begin, col_end+1):
                result.append(matrix[row_begin][i])
            row_begin += 1
            
            # Traverse the last column from top to bottom
            for i in range(row_begin, row_end+1):
                result.append(matrix[i][col_end])
            col_end -= 1
            
            # Traverse the last row from right to left
            if row_begin <= row_end:
                for i in range(col_end, col_begin-1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
                
            # Traverse the first column from bottom to top
            if col_begin <= col_end:
                for i in range(row_end, row_begin-1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1
        
        return result
