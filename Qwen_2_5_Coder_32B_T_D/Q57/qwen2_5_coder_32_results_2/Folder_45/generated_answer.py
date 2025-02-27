import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for di in range(i, rows):
                for dj in range(j, cols):
                    submatrix = matrix[i:di + 1, j:dj + 1]
                    if submatrix.sum() == -77:
                        result.append(submatrix.tolist())
    return result