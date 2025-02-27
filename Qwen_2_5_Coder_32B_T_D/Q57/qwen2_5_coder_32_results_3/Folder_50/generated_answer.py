import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(submat):
        return np.sum(submat)
    submatrices = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submat = matrix[start_row:end_row, start_col:end_col]
                    if sum_submatrix(submat) == 95:
                        submatrices.append(submat)
    return submatrices