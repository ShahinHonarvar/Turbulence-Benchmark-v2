import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sum_required = -82
    valid_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.sum() == sum_required:
                        valid_submatrices.append(submatrix)
    return valid_submatrices