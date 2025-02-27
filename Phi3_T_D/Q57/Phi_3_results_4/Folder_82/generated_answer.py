import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                for k in range(i, i + size):
                    for l in range(j, j + size):
                        if np.sum(matrix[i:i + size, j:j + size]) == -27:
                            result.append(matrix[i:i + size, j:j + size].copy())
    return result