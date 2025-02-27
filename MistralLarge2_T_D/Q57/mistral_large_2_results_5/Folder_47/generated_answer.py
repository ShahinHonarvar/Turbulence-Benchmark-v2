import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []

    def get_submatrices(start_row, start_col):
        for end_row in range(start_row, m):
            for end_col in range(start_col, n):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                if np.sum(submatrix) == 27:
                    submatrices.append(submatrix)
    for i in range(m):
        for j in range(n):
            get_submatrices(i, j)
    return submatrices