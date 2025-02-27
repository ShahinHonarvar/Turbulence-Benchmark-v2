import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for i2 in range(i, rows):
                for j2 in range(j, cols):
                    submatrix = matrix[i:i2 + 1, j:j2 + 1]
                    if np.sum(submatrix) == 35:
                        result.append(submatrix)
    return result