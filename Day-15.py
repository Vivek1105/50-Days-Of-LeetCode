# Problem - 1572. Matrix Diagonal Sum




class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n):
            sum += mat[i][i]
            if i != n-1-i:
                sum += mat[i][n-1-i]
        return sum
