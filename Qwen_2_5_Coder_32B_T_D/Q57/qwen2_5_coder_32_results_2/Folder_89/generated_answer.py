import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if np.sum(matrix[i:r + 1, j:c + 1]) == 80:
                        result.append(matrix[i:r + 1, j:c + 1])
    return result