import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_target = 54
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if submatrix.sum() == sum_target:
                        submatrices.append(submatrix)
    return submatrices