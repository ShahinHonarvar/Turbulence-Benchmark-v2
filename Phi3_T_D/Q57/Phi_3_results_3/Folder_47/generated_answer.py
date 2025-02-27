import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submat = matrix[i:j + 1, k:l + 1]
                    if submat.sum() == 27:
                        result.append(submat)
    return result