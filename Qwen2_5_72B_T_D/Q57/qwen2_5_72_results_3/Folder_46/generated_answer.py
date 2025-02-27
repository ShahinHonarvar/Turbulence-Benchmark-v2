import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(matrix, start_row, end_row, start_col, end_col):
        return matrix[start_row:end_row, start_col:end_col]

    def sum_equal_to_target(submatrix, target=416):
        return np.sum(submatrix) == target
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = get_submatrix(matrix, start_row, end_row, start_col, end_col)
                    if sum_equal_to_target(submatrix):
                        result.append(submatrix)
    return result