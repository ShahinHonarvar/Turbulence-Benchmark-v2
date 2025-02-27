import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        return np.sum(mat[start_row:end_row, start_col:end_col])
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if sum_submatrix(matrix, start_row, start_col, end_row, end_col) == -46:
                        result.append(matrix[start_row:end_row, start_col:end_col])
    return result