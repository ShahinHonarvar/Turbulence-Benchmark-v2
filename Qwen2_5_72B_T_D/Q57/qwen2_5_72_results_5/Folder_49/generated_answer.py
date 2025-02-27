import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, top_row, left_col, bottom_row, right_col):
        sum_val = 0
        for i in range(top_row, bottom_row + 1):
            for j in range(left_col, right_col + 1):
                sum_val += mat[i][j]
        return sum_val
    rows, cols = matrix.shape
    result = []
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if sum_submatrix(matrix, i, j, i + size - 1, j + size - 1) == -42:
                    result.append(matrix[i:i + size, j:j + size])
    return result