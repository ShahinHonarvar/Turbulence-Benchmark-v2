import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_equal_to_target(submat, target=-50):
        return np.sum(submat) == target
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    submat = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if is_sum_equal_to_target(submat):
                        submatrices.append(submat.tolist())
    return submatrices