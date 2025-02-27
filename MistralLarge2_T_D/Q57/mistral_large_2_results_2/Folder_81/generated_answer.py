import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for start_row in range(n):
        for start_col in range(m):
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    if np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1]) == -90:
                        submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1].tolist())
    return submatrices