import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, end_row, start_col, end_col):
        return np.sum(mat[start_row:end_row, start_col:end_col])
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    if sum_submatrix(matrix, start_row, end_row, start_col, end_col) == 901:
                        result.append(matrix[start_row:end_row, start_col:end_col])
    return result