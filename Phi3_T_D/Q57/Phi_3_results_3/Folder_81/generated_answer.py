import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for size_i in range(i, rows):
                for size_j in range(j, cols):
                    submat = matrix[i:size_i + 1, j:size_j + 1]
                    if np.sum(submat) == -90:
                        result.append(submat)
    return result