import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 69
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for r in range(i + 1, matrix.shape[0] + 1):
                for c in range(j + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[i:r, j:c] == n) == n:
                        count += 1
    return count