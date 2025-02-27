import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        total = 0
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                total += mat[i][j]
        return total
    target_sum = -46
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if sum_submatrix(matrix, start_row, start_col, end_row, end_col) == target_sum:
                        result.append(matrix[start_row:end_row, start_col:end_col])
    return result