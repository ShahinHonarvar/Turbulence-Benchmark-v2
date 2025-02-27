import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        return mat[start_row:end_row, start_col:end_col].sum()
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if sum_submatrix(matrix, start_row, start_col, end_row, end_col) == -20:
                        result.append(matrix[start_row:end_row, start_col:end_col])
    return result