import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row_idx, row in enumerate(matrix):
        for col_idx, _ in enumerate(row):
            submatrix = matrix[row_idx:, col_idx:]
            submatrix_sum = np.sum(submatrix)
            if submatrix_sum == -81:
                submatrices.append(submatrix)
    return submatrices