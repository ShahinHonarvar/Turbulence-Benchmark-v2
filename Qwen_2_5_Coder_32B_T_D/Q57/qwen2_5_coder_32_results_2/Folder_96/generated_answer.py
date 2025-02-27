import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for n in range(i, rows):
                for m in range(j, cols):
                    if np.sum(matrix[i:n + 1, j:m + 1]) == -63:
                        result.append(matrix[i:n + 1, j:m + 1])
    return result