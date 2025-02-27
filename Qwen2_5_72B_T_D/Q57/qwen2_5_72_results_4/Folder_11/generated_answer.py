import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        sum_val = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sum_val += mat[i][j]
        return sum_val
    rows, cols = matrix.shape
    result = []
    for size in range(1, max(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                if sum_submatrix(matrix, row, col, row + size - 1, col + size - 1) == 38:
                    result.append(matrix[row:row + size, col:col + size])
    return result