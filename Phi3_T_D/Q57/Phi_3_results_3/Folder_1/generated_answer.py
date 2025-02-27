import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    submat = matrix[i1:i2 + 1, j1:j2 + 1]
                    if submat.sum() == -25:
                        result.append(submat)
    return result