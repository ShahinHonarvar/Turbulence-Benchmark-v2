import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_submatrices(start_row, start_col):
        for end_row in range(start_row, rows):
            for end_col in range(start_col, cols):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                if np.sum(submatrix) == -9:
                    result.append(submatrix)
    for i in range(rows):
        for j in range(cols):
            get_submatrices(i, j)
    return result