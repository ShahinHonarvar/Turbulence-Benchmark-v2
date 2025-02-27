import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_equal_to_target(submatrix, target=-87):
        return np.sum(submatrix) == target
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if is_sum_equal_to_target(submatrix):
                        result.append(submatrix)
    return result