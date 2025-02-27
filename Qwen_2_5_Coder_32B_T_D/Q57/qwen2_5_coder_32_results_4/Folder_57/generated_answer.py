import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for k in range(j, cols):
                    if np.sum(matrix[i:h + 1, j:k + 1]) == 13:
                        result.append(matrix[i:h + 1, j:k + 1])
    return result