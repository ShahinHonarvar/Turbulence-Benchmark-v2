import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_submatrix_sum(start_row, end_row, start_col, end_col):
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    if get_submatrix_sum(start_row, end_row, start_col, end_col) == -46:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return result