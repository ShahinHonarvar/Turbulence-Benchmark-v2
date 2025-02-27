import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    submat = matrix[i:r + 1, j:c + 1]
                    if np.sum(submat) == -10:
                        result.append(submat)
    return result