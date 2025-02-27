import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(mat, start_row, end_row, start_col, end_col):
        sum_val = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sum_val += mat[i][j]
        return sum_val
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    if sum_of_submatrix(matrix, start_row, end_row, start_col, end_col) == -6:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return result