import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def check_submatrix_sum(start_row, start_col, end_row, end_col):
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if check_submatrix_sum(start_row, start_col, end_row, end_col) == 398:
                        submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return submatrices