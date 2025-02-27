import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = matrix[i:k + 1, j:l + 1]
                    if np.sum(submat) == 13:
                        results.append(submat)
    return results