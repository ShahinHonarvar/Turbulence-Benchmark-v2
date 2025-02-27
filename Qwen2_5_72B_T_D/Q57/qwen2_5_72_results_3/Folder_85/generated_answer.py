import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        sum_val = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sum_val += mat[i][j]
        return sum_val
    m, n = matrix.shape
    result = []
    for size in range(1, min(m, n) + 1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if sum_submatrix(matrix, i, j, i + size - 1, j + size - 1) == -87:
                    result.append(matrix[i:i + size, j:j + size].tolist())
    return result