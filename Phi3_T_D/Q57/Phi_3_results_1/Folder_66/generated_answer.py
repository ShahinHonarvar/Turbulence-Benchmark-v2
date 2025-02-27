import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_target = 99
    submatrices = []
    rows, cols = matrix.shape
    for y1 in range(rows):
        for y2 in range(y1, rows):
            for x1 in range(cols):
                for x2 in range(x1, cols):
                    submatrix = matrix[y1:y2 + 1, x1:x2 + 1]
                    if submatrix.sum() == sum_target:
                        submatrices.append(submatrix)
    return submatrices