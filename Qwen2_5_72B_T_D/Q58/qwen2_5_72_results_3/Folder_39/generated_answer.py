import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 59
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if np.sum(matrix[i:, j:] >= n) == n:
                count += 1
    return count