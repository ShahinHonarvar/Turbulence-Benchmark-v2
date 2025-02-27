import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for end_i in range(i, rows):
                for end_j in range(j, cols):
                    submatrix = matrix[i:end_i + 1, j:end_j + 1]
                    if np.sum(submatrix) == 15:
                        result.append(submatrix)
    return result