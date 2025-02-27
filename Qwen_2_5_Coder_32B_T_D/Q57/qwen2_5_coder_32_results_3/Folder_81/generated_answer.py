import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_i in range(i, rows):
                for sub_j in range(j, cols):
                    if np.sum(matrix[i:sub_i + 1, j:sub_j + 1]) == -90:
                        result.append(matrix[i:sub_i + 1, j:sub_j + 1])
    return result