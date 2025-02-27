import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col):
        for r in range(start_row, rows):
            for c in range(start_col, cols):
                submatrix = matrix[start_row:r + 1, start_col:c + 1]
                if np.sum(submatrix) == 34:
                    submatrices.append(submatrix)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j)
    return submatrices