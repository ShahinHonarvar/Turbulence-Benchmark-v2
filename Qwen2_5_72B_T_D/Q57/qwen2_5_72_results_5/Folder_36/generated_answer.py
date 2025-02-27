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
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if sum_submatrix(matrix, start_row, start_col, end_row, end_col) == -779:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return result