import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_i in range(i + 1, rows + 1):
                for sub_j in range(j + 1, cols + 1):
                    submatrix = matrix[i:sub_i, j:sub_j]
                    if np.sum(submatrix) == -10:
                        result.append(submatrix)
    return result