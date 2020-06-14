# problem link: https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        num_r = len(matrix)
        num_c = len(matrix[0])
        def check_one_diag(r, c):
            prev_val = matrix[r][c]
            while r < num_r and c < num_c:
                if matrix[r][c] != prev_val:
                    return False
                r += 1
                c += 1
            return True
        for c in range(num_c):
            if not check_one_diag(0, c):
                return False
        for r in range(1, num_r):
            if not check_one_diag(r, 0):
                return False
        return True