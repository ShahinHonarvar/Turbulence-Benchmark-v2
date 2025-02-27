import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_equal(submatrix, target_sum):
        return np.sum(submatrix) == target_sum
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if is_sum_equal(submatrix, 830):
                        result.append(submatrix)
    return result