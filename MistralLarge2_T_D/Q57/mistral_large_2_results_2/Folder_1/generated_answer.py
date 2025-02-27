import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col):
        for end_row in range(start_row, n):
            for end_col in range(start_col, m):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                if np.sum(submatrix) == -25:
                    submatrices.append(submatrix)
    for i in range(n):
        for j in range(m):
            find_submatrices(i, j)
    return submatrices