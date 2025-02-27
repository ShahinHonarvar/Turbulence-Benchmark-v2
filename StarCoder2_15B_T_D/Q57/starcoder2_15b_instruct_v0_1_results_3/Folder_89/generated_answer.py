import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 80:
                submatrices.append(submatrix)
    return submatrices