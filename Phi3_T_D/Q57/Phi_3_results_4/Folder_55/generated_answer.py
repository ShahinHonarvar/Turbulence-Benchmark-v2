import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size_r in range(i + 1, rows + 1):
                for size_c in range(j + 1, cols + 1):
                    submatrix = matrix[i:size_r, j:size_c]
                    if np.sum(submatrix) == 1:
                        result.append(submatrix)
    return result