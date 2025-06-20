import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -308
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices